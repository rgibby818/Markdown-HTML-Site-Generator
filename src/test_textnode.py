import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a textnode", TextType.BOLD)
        node2 = TextNode("this is a textnode", TextType.BOLD)

        node3 = TextNode("this is a textnode", TextType.CODE, "https://www.boot.dev")
        node4 = TextNode("this is a textnode", TextType.CODE, "https://www.boot.dev")

        self.assertEqual(node, node2, msg="\nFAILED TEST: node and node2 objects failed Equal operator.")
        self.assertEqual(node3, node4, msg="\nFAILED TEST: node3 and node4 objects failed Equal operator.")

    def test_not_eq(self):
        node = TextNode(
            "textnode with text that is different", TextType.ITALIC
        )
        node2 = TextNode(
            "textnode with text that is different...", TextType.ITALIC
        )

        node3 = TextNode(
            "textnode with different TextType", TextType.BOLD
        )
        node4 = TextNode(
            "textnode with different TextType", TextType.ITALIC
        )

        node5 = TextNode(
            "textnode with different url", TextType.BOLD, "https://www.google.com"
        )
        node6 = TextNode(
            "textnode with different url", TextType.BOLD, "https://www.yahoo.com"
        )

        self.assertNotEqual(node, node2, msg="\nFAILED TEST: node and node2 objects failed NotEqual operator")
        self.assertNotEqual(node3, node4, msg="\nFAILED TEST: node3 and node4 objects failed NotEqual operator")
        self.assertNotEqual(node5, node6, msg="\nFAILED TEST: node5 and node6 objects failed NotEqual operator")

    def test_is(self):
        node = TextNode(
            "textnode with none as url", TextType.BOLD
        )
        self.assertIs(node.url, None, msg="\nFAILED TEST: node url is not None")

if __name__ == "__main__":
    unittest.main()
