import unittest
from src.blocks import markdown_to_blocks


class Test_blocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                "- This is the first list item in a list block\n- This is a list item\n- This is another list item",
            ],
            blocks,
        )
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        md = """
# This is a heading




**Bold** text with a `code block`
    Some more random text
"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            [
                "# This is a heading",
                "**Bold** text with a `code block`\n    Some more random text",
            ],
        )


if __name__ == "__main__":
    unittest.main()
