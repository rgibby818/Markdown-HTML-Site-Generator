import unittest
from src.htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):

        node1 = LeafNode("p", "This is a test", None)  # Test 1
        node2 = LeafNode("a", "Click Me", {"href": "https://www.example.com"})  # Test 2

        # Test 1: .to_html() should output expected output.
        self.assertEqual(
            node1.to_html(),  # Method call
            "<p>This is a test</p>",  # Expected output
            msg="\nFAILED TEST: to_html() method failed (node1) did not pass assertEqual",  # Error message
        )

        # Test 2: .to_html() should output expected output.
        self.assertEqual(
            node2.to_html(),  # Method call
            '<a href="https://www.example.com">Click Me</a>',  # Expected output
            msg="\nFAILED TEST: to_html() method failed (node2) did not pass assertEqual",  # Error message
        )

    def test_errors(self):
        # Test 1: .to_html() should raise a ValueError because node3.value does not contain a value.
        with self.assertRaises(
            ValueError,  # Expected exception
            msg="\nFAILED TEST: to_html() method failed(node3) did not pass assertRaise",
        ):
            node1 = LeafNode(None, None, None)  # Test 1


if __name__ == "__main__":
    unittest.main()
