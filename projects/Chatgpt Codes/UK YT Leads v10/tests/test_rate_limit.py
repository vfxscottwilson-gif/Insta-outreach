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


class RowsChangedTests(unittest.TestCase):
    def test_append_survives_rows_added_by_a_human_during_the_run(self):
        sheet = Sheets.__new__(Sheets)
        header = ['Channel ID', 'Contact ID']
        sheet.headers = {'T': header}
        sheet.rows = {'T': [['a', 'one']]}
        sheet.tabs = {'T': {'gridProperties': {'rowCount': 1000}, 'sheetId': 1}}
        sheet.read = lambda title: [header, ['a', 'one'], ['h', 'human']]   # a row appeared
        written = []
        sheet.write = lambda title, cell, values, formula=False: written.append((cell, values))
        sheet.repair_ids = lambda *a, **k: None
        block = sheet.append('T', [{'Channel ID': 'b', 'Contact ID': 'two'}, {'Channel ID': 'a', 'Contact ID': 'one'}])
        self.assertEqual(block, (4, 4))                    # lands below the human's row
        self.assertEqual(written[0], ('A4', [['b', 'two']]))   # the duplicate lead was skipped


class ReorderTests(unittest.TestCase):
    def test_old_order_is_moved_by_header_name_and_extras_are_kept(self):
        from src.sheets import reorder
        expected = ['ID', 'Email', 'Guessed Email', 'Niche', 'Score']
        header = ['ID', 'Niche', 'Email', 'My Notes', 'Score']
        rows = [[1, 'Tech', 'a@b.com', 'call him', 90]]
        new_header, new_rows = reorder(header, rows, expected)
        self.assertEqual(new_header, ['ID', 'Email', 'Guessed Email', 'Niche', 'Score', 'My Notes'])
        self.assertEqual(new_rows, [[1, 'a@b.com', '', 'Tech', 90, 'call him']])

    def test_already_ordered_or_duplicate_headers_are_left_alone(self):
        from src.sheets import reorder
        self.assertIsNone(reorder(['ID', 'Email', 'Extra'], [], ['ID', 'Email', 'Niche']))
        self.assertIsNone(reorder(['ID', 'ID'], [], ['ID']))
