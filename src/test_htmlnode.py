import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()  # Test 1
        node2 = HTMLNode()  # Test 1

        # Test 1: Both node/node2 should return true when compared to each other.
        self.assertEqual(
            node, node2, msg="\nFAILED TEST: node and node2 objects are not equal"
        )

    def test_props_to_html(self):
        # Test 1
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        # Test 1: .props_to_html() should match expected output
        self.assertEqual(
            node.props_to_html(),  # Method call
            ' href="https://www.google.com" target="_blank"',  # Expected output
            msg="\nFAILED TEST: props_to_html method for (node) does not return expected string",  # Error message.
        )

        # Test 2
        node2 = HTMLNode(props={"href": "https://www.boot.dev", "id": "1"})
        self.assertEqual(
            node2.props_to_html(),
            ' href="https://www.boot.dev" id="1"',
            msg="\nFAILED TEST: props_to_html method for (node2) does not return expected string",
        )

    def test_repr(self):
        node = HTMLNode()
        self.assertEqual(
            repr(node),
            "HTMLNode(None, None, None, None)",
            msg="\nFAILED TEST: __repr__ does not print expected output",
        )


if __name__ == "__main__":
    unittest.main()
