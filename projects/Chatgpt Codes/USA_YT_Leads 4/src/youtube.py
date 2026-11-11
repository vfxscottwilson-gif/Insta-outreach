import time

class BudgetStop(Exception):
    pass

class YouTubeError(Exception):
    pass

class YouTube:
    def __init__(self, key, cfg, metrics, session=None):
        self.key, self.cfg, self.metrics = key, cfg, metrics
        if session is None:
            import requests
            session = requests.Session()
        self.session = session

    def get(self, endpoint, **params):
        search = endpoint == 'search'
        for attempt in range(3):
            if self.metrics['search_calls'] >= self.cfg['max_searches'] and search:
                raise BudgetStop('Search budget reached')
            if not search and self.metrics['other_api_calls'] >= self.cfg['other_api_units_budget']:
                raise BudgetStop('Inspection budget reached')
            self.metrics['search_calls' if search else 'other_api_calls'] += 1
            import requests
            try:
                response = self.session.get('https://www.googleapis.com/youtube/v3/' + endpoint,
                        params={**params, 'key': self.key}, timeout=25)
                data = response.json()
            except (requests.RequestException, ValueError):
                self.metrics['failed_requests'] += 1
                if attempt == 2:
                    raise YouTubeError('YouTube network or response failure') from None
            else:
                if response.ok:
                    return data
                reasons = [e.get('reason', '') for e in data.get('error', {}).get('errors', [])]
                self.metrics['failed_requests'] += 1
                if any(r in ('quotaExceeded', 'dailyLimitExceeded') for r in reasons):
                    raise BudgetStop('Provider quota reached')
                if response.status_code not in (429, 500, 502, 503, 504):
                    raise YouTubeError(f'YouTube HTTP {response.status_code}; check key and enabled API')
                if attempt == 2:
                    raise YouTubeError('YouTube temporarily unavailable')
            self.metrics['retries'] += 1
            time.sleep(2 ** attempt)

    def channels(self, ids):
        if not ids:
            return {}
        data = self.get('channels', part='snippet,statistics,contentDetails', id=','.join(ids), maxResults=50)
        return {c['id']: c for c in data.get('items', [])}

    def videos(self, playlist):
        from .qualification import duration
        videos, token = [], None
        complete = False
        for _ in range(self.cfg['max_upload_pages']):
            params = dict(part='contentDetails', playlistId=playlist, maxResults=50)
            if token:
                params['pageToken'] = token
            page = self.get('playlistItems', **params)
            ids = [x['contentDetails']['videoId'] for x in page.get('items', [])]
            if ids:
                data = self.get('videos', part='snippet,statistics,contentDetails', id=','.join(ids))
                for item in data.get('items', []):
                    # Ongoing streams have no stable duration and are not upload evidence.
                    if item['snippet'].get('liveBroadcastContent') in ('live', 'upcoming'):
                        continue
                    videos.append(dict(id=item['id'], title=item['snippet']['title'],
                        description=item['snippet'].get('description', ''),
                        published=item['snippet']['publishedAt'],
                        language=item['snippet'].get('defaultAudioLanguage') or item['snippet'].get('defaultLanguage', ''),
                        seconds=duration(item['contentDetails'].get('duration', '')),
                        views=int(item.get('statistics', {}).get('viewCount', 0))))
            token = page.get('nextPageToken')
            longs = [v for v in videos if v['seconds'] > self.cfg['long_video_min_seconds_exclusive']]
            # Need BOTH the view sample and complete activity coverage through the cutoff.
            from .models import utcnow, parse
            from datetime import timedelta
            cutoff = utcnow() - timedelta(days=self.cfg['activity_days'])
            covered = any(parse(v['published']) < cutoff for v in videos)
            if not token or (len(longs) >= self.cfg['video_sample_size'] and covered):
                complete = True
                break
        videos.sort(key=lambda v: v['published'], reverse=True)
        return videos, complete
