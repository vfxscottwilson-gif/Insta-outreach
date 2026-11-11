import re
from datetime import timedelta
from .models import parse, utcnow

def duration(value):
    match = re.fullmatch(r'P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', value)
    if not match:
        return 0
    d, h, m, s = [int(x or 0) for x in match.groups()]
    return d * 86400 + h * 3600 + m * 60 + s

def precheck(channel, cfg):
    stats = channel.get('statistics', {})
    if stats.get('hiddenSubscriberCount') or 'subscriberCount' not in stats:
        return 'review', 'Subscriber count unavailable'
    if not cfg['min_subscribers'] <= int(stats['subscriberCount']) <= cfg['max_subscribers']:
        return 'rejected', 'Subscriber count outside configured range'
    country = channel['snippet'].get('country', '')
    if country and country not in cfg.get('countries', ['US']):
        return 'rejected', 'Channel country metadata is not ' + '/'.join(cfg.get('countries', ['US']))
    return '', ''

def evaluate(channel, videos, complete, cfg, niches, confirmed=False):
    cutoff = utcnow() - timedelta(days=cfg['activity_days'])
    longs = [v for v in videos if v['seconds'] > cfg['long_video_min_seconds_exclusive']]
    sample = longs[:cfg['video_sample_size']]
    active = [v for v in longs if parse(v['published']) >= cutoff]
    hits = sum(v['views'] >= cfg['min_video_views'] for v in sample)
    reasons, failures = [], []
    if hits < cfg['min_videos_above_threshold']:
        (failures if complete else reasons).append('Fewer than two sampled long videos meet view threshold')
    if len(active) < cfg['min_long_uploads']:
        (failures if complete else reasons).append('Insufficient long uploads in activity window')
    if not channel['snippet'].get('country'):
        reasons.append('/'.join(cfg.get('countries', ['US'])) + ' location not established by channel country metadata')
    text = ' '.join([channel['snippet']['title'], channel['snippet'].get('description', '')]
                    + [v['title'] for v in sample]).lower()
    scored = [(sum(text.count(s.lower()) for s in n['signals']), n['name']) for n in niches]
    best = max(scored, default=(0, ''))
    niche = best[1] if best[0] else ''
    if not niche:
        reasons.append('Niche not established; requires review')
    if cfg['require_talking_head_confirmation'] and not confirmed:
        reasons.append('Talking head format requires visual confirmation')
    if not complete:
        reasons.append('Upload inspection cap reached; sample or activity coverage may be incomplete')
    in_window = [v for v in videos if parse(v['published']) >= cutoff]
    status = 'rejected' if failures else ('review' if reasons else 'qualified')
    return dict(status=status, reason='; '.join(failures or reasons), niche=niche,
        sample=sample, active=active, videos_above=hits, videos_checked=len(sample),
        average_views=round(sum(v['views'] for v in sample) / len(sample)) if sample else '',
        last_upload=longs[0]['published'] if longs else '',
        uploads_in_window=len(in_window), shorts_in_window=len(in_window) - len(active))
