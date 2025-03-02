import unittest

from src.extract_markdown import extract_markdown_images, extract_markdown_links

class TestMarkdownImages(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        no_matches = extract_markdown_images(
            "This is text with a [link](https://www.google.com)"
        )
        multiple_matches = extract_markdown_images(
            "This is text with a ![image](https://www.image.com) and another ![image2](https://www.image2.com)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        self.assertListEqual([], extract_markdown_images(""))
        self.assertListEqual([], no_matches)
        self.assertListEqual(
            [("image", "https://www.image.com"), ("image2", "https://www.image2.com")], multiple_matches
            )


class TestMarkdownLinks(unittest.TestCase):

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com)"
        )
        no_match = extract_markdown_links(
            "This is text with a ![image](https://www.image.com/image.png)"
        )
        multiple_matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com) and another [link2](https://www.duckduckgo.com)"
        )
        self.assertListEqual([("link", "https://www.google.com")], matches)
        self.assertListEqual([], extract_markdown_links(""))
        self.assertListEqual([], no_match)
        self.assertListEqual([("link", "https://www.google.com"), ("link2", "https://www.duckduckgo.com")], multiple_matches
                             )



