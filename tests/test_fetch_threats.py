import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / 'scripts' / 'fetch_threats.py'

spec = importlib.util.spec_from_file_location('fetch_threats', MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class FetchThreatsTests(unittest.TestCase):
    def test_clean_item_removes_empty_and_blank_values(self):
        item = module.clean_item({
            'title': '   ',
            'link': 'https://example.com/1',
            'summary': '  ',
            'source': 'Source Test',
            'published': 'Wed, 16 Sep 2026 21:20:59 +0530',
        })
        self.assertIsNone(item)

    def test_clean_item_normalizes_summary_and_dates(self):
        item = module.clean_item({
            'title': '  Example incident  ',
            'link': 'https://example.com/2',
            'summary': '  Active exploitation was observed in a web app.  ',
            'source': '  Example Source  ',
            'published': 'Wed, 16 Sep 2026 21:20:59 +0530',
        })

        self.assertIsNotNone(item)
        self.assertEqual(item['title'], 'Example incident')
        self.assertEqual(item['summary'], 'Active exploitation was observed in a web app.')
        self.assertEqual(item['source'], 'Example Source')
        self.assertIn('2026-09-16', item['published'])

    def test_dedupe_items_removes_duplicate_titles_and_links(self):
        items = [
            {'title': 'Alpha', 'link': 'https://example.com/a', 'source': 'A', 'published': '2026-09-16T00:00:00Z', 'summary': 'One'},
            {'title': 'Alpha', 'link': 'https://example.com/a', 'source': 'A', 'published': '2026-09-16T00:00:00Z', 'summary': 'One'},
            {'title': 'Beta', 'link': 'https://example.com/b', 'source': 'B', 'published': '2026-09-15T00:00:00Z', 'summary': 'Two'},
        ]

        cleaned = module.dedupe_items(items)
        self.assertEqual(len(cleaned), 2)
        self.assertEqual([item['title'] for item in cleaned], ['Alpha', 'Beta'])


if __name__ == '__main__':
    unittest.main()
