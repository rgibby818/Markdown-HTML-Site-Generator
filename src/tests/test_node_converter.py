import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import unittest

from node_converter import text_node_to_html_node
from textnode import TextNode, TextType
from leafnode import LeafNode

text_node_to_html_node_error_message = (
    "FAILED TEST: text_node_to_html_node() did not output the correct output"
)


class Test_Text_to_Html_Node(unittest.TestCase):

    # Test Normal TextNode Conversions
    def text_node_to_html_node_normal(self):
        normal_text = text_node_to_html_node(
            TextNode(text="Normal", text_type=TextType.NORMALE, url=None)
        )

        # Test Normal 1
        self.assertEqual(
            normal_text,
            LeafNode(tag=None, value="Normal", props=None),
            msg=text_node_to_html_node_error_message,
        )

    # Test Bold TextNode Conversions
    def test_text_node_to_html_node_bold(self):
        bold_text = text_node_to_html_node(
            TextNode(text="Bold Text", text_type=TextType.BOLD, url=None)
        )
        # Test Bold 1
        self.assertEqual(
            bold_text,
            LeafNode(tag="b", value="Bold Text", props=None),
            msg=text_node_to_html_node_error_message,
        )

    # Test Italics TextNode Conversions
    def test_text_node_to_html_node_italics(self):
        italic_text = text_node_to_html_node(
            TextNode(text="Italic Text", text_type=TextType.ITALIC, url=None)
        )
        # Test Italics 1
        self.assertEqual(
            italic_text,
            LeafNode(tag="i", value="Italic Text", props=None),
            msg=text_node_to_html_node_error_message,
        )

    # Test Code TextNode Conversions
    def test_text_node_to_html_node_code(self):
        code_text = text_node_to_html_node(
            TextNode(text="Code Text", text_type=TextType.CODE, url=None)
        )

        # Test Code 1
        self.assertEqual(
            code_text,
            LeafNode(tag="code", value="Code Text", props=None),
            msg=text_node_to_html_node_error_message,
        )

    # Test Link TextNode Conversions
    def test_text_node_to_html_node_links(self):
        link_text = text_node_to_html_node(
            TextNode("Link Text", TextType.LINKS, url="https://www.example.com")
        )

        # Test Link 1
        self.assertEqual(
            link_text,
            LeafNode(
                tag="a", value="Link Text", props={"href": "https://www.example.com"}
            ),
            msg=text_node_to_html_node_error_message,
        )

    # Test Image TextNode Conversions
    def test_text_node_to_html_node_images(self):
        image_text = text_node_to_html_node(
            TextNode(
                "Image of a cat", TextType.IMAGES, url="https://www.image-of-a-cat.com"
            )
        )

        self.assertEqual(
            image_text,
            LeafNode(
                tag="img",
                value="",
                props={
                    "src": "https://www.image-of-a-cat.com",
                    "alt": "Image of a cat",
                },
            ),
            msg=text_node_to_html_node_error_message,
        )
    
    # Test Error Checking for TextNode
    def test_text_node_to_html_node_error_checking(self):
        with self.assertRaises(
            TypeError,
            msg=text_node_to_html_node_error_message,
        ):
            error_node = text_node_to_html_node(LeafNode(tag="p", value="P tag"))

if __name__ == "__main__":
    unittest.main()
