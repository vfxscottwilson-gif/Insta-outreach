import unittest
from unittest import mock
from src.sheets import Sheets, SheetsError


class FakeResponse:
    def __init__(self, status): self.status_code, self.ok = status, status < 400
    def json(self): return {'error': {'status': 'RESOURCE_EXHAUSTED', 'message': 'quota'}} if not self.ok else {}


class RateLimitTests(unittest.TestCase):
    def make(self, statuses):
        sheet = Sheets.__new__(Sheets)
        sheet.base = 'https://x/'
        replies = iter(statuses)
        sheet.session = mock.Mock(request=lambda *a, **k: FakeResponse(next(replies)))
        return sheet

    def test_429_waits_then_succeeds(self):
        with mock.patch('src.sheets.time.sleep') as sleep:
            self.assertEqual(self.make([429, 429, 200]).call('POST', '/values:batchUpdate', body={}, retry=False), {})
        self.assertIn(mock.call(30), sleep.call_args_list)

    def test_429_gives_up_with_clear_error(self):
        with mock.patch('src.sheets.time.sleep'):
            with self.assertRaises(SheetsError):
                self.make([429] * 9).call('POST', '/values:batchUpdate', body={}, retry=False)

if __name__ == '__main__':
    unittest.main()
