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

if __name__ == "__main__":
    unittest.main()
