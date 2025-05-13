import unittest

from src.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):

    def test_extract_title_success(self):
        markdown = """
# This is a heading
**This is Bold**
"""
        self.assertEqual(extract_title(markdown), "This is a heading")

    def test_extract_title_failure(self):
        markdown = """
this is a markdown file that does not contian a header
## Header 2
### Header 3
`code block`"""
        with self.assertRaises(ValueError):
            extract_title(markdown)
