import unittest
from src.blocks import markdown_to_blocks, block_to_block_type, BlockType
from src.markdown_to_html import *


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

    def test_block_to_block_type(self):
        block = "# Heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block = """
``` Int main(void) {
    printf("Hello, World!");
    return 0
}
```
"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

        block = """
> quote
> another quote
>also a quote
"""
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

        block = """
- unorderd list item 1
- unordered list item 2
- unorederd list item 3
"""
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

        block = """
1. ordered list item 1
2. ordered list item 2
3. ordered list item 3
"""
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

        block = "This is a paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

        block = """
1.This should be a paragraph because of incorrect formatting
2. Ordered list item 2
"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


if __name__ == "__main__":
    unittest.main()
