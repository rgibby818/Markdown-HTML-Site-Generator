import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import unittest

from src.htmlnode import LeafNode, HTMLNode
from src.textnode import TextType, TextNode, text_node_to_html_node
text_node_error_message = "FAILED TEST: TextNode did not output the correct output"

text_node_to_html_node_error_message = (
    "FAILED TEST: text_node_to_html_node() did not output the correct output"
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a textnode", TextType.BOLD)
        node2 = TextNode("this is a textnode", TextType.BOLD)

        node3 = TextNode("this is a textnode", TextType.CODE, "https://www.boot.dev")
        node4 = TextNode("this is a textnode", TextType.CODE, "https://www.boot.dev")

        self.assertEqual(
            node,
            node2,
            msg=text_node_error_message,
        )
        self.assertEqual(
            node3,
            node4,
            msg=text_node_error_message,
        )

    def test_not_eq(self):
        node = TextNode("textnode with text that is different", TextType.ITALIC)
        node2 = TextNode("textnode with text that is different...", TextType.ITALIC)

        node3 = TextNode("textnode with different TextType", TextType.BOLD)
        node4 = TextNode("textnode with different TextType", TextType.ITALIC)

        node5 = TextNode(
            "textnode with different url", TextType.BOLD, "https://www.google.com"
        )
        node6 = TextNode(
            "textnode with different url", TextType.BOLD, "https://www.yahoo.com"
        )

        self.assertNotEqual(
            node,
            node2,
            msg=text_node_error_message,
        )
        self.assertNotEqual(
            node3,
            node4,
            msg=text_node_error_message,
        )
        self.assertNotEqual(
            node5,
            node6,
            msg=text_node_error_message,
        )

    def test_is(self):
        node = TextNode("textnode with none as url", TextType.BOLD)
        self.assertIs(node.url, None, msg=text_node_error_message)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGES, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

# class Test_Text_to_Html_Node(unittest.TestCase):

#     # Test Normal TextNode Conversions
#     def text_node_to_html_node_normal(self):
#         normal_text = text_node_to_html_node(
#             TextNode(text="Normal", text_type=TextType.NORMAL, url=None)
#         )

#         # Test Normal 1
#         self.assertEqual(
#             normal_text,
#             LeafNode(tag=None, value="Normal", props=None),
#             msg=text_node_to_html_node_error_message,
#         )

#     # Test Bold TextNode Conversions
#     def test_text_node_to_html_node_bold(self):
#         bold_text = text_node_to_html_node(
#             TextNode(text="Bold Text", text_type=TextType.BOLD, url=None)
#         )
#         # Test Bold 1
#         self.assertEqual(
#             bold_text,
#             LeafNode(tag="b", value="Bold Text", props=None),
#             msg=text_node_to_html_node_error_message,
#         )

#     # Test Italics TextNode Conversions
#     def test_text_node_to_html_node_italics(self):
#         italic_text = text_node_to_html_node(
#             TextNode(text="Italic Text", text_type=TextType.ITALIC, url=None)
#         )
#         # Test Italics 1
#         self.assertEqual(
#             italic_text,
#             LeafNode(tag="i", value="Italic Text", props=None),
#             msg=text_node_to_html_node_error_message,
#         )

#     # Test Code TextNode Conversions
#     def test_text_node_to_html_node_code(self):
#         code_text = text_node_to_html_node(
#             TextNode(text="Code Text", text_type=TextType.CODE, url=None)
#         )

#         # Test Code 1
#         self.assertEqual(
#             code_text,
#             LeafNode(tag="code", value="Code Text", props=None),
#             msg=text_node_to_html_node_error_message,
#         )

#     # Test Link TextNode Conversions
#     def test_text_node_to_html_node_links(self):
#         link_text = text_node_to_html_node(
#             TextNode("Link Text", TextType.LINKS, url="https://www.example.com")
#         )

#         # Test Link 1
#         self.assertEqual(
#             link_text,
#             LeafNode(
#                 tag="a", value="Link Text", props={"href": "https://www.example.com"}
#             ),
#             msg=text_node_to_html_node_error_message,
#         )

#     # Test Image TextNode Conversions
#     def test_text_node_to_html_node_images(self):
#         image_text = text_node_to_html_node(
#             TextNode(
#                 "Image of a cat", TextType.IMAGES, url="https://www.image-of-a-cat.com"
#             )
#         )

#         self.assertEqual(
#             image_text,
#             LeafNode(
#                 tag="img",
#                 value="",
#                 props={
#                     "src": "https://www.image-of-a-cat.com",
#                     "alt": "Image of a cat",
#                 },
#             ),
#             msg=text_node_to_html_node_error_message,
#         )
    
#     # Test Error Checking for TextNode
#     def test_text_node_to_html_node_error_checking(self):
#         with self.assertRaises(
#             TypeError,
#             msg=text_node_to_html_node_error_message,
#         ):
#             error_node = text_node_to_html_node(LeafNode(tag="p", value="P tag"))

if __name__ == "__main__":
    unittest.main()
