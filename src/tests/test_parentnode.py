import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from src.parentnode import ParentNode
from src.leafnode import LeafNode

import unittest


class TestParentNode(unittest.TestCase):

    def test_to_html(self):
        # Test 1: node should output expected output.
        # <p> Parent->child->child->child->child
        #   <b>Bold text</b>Normal text<i>italic text</i>
        # </p>
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            msg="FAILED TEST: node does not output expected output.",
        )

        # Test 2: node2 should output expected output.
        # <div>
        #     <span>
        #         <p>Paragraph text</p>
        #     </span>
        #     <p>
        #         Normal text<b>Bold text</b><i>italic text</i>
        #     </p>
        # </div>
        node2 = ParentNode(
            "div",
            [
                ParentNode(
                    "span", [ParentNode("p", [LeafNode(None, "Paragraph text")])]
                ),
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "Normal text"),
                        LeafNode("b", "Bold text"),
                        LeafNode("i", "italic text"),
                    ],
                ),
            ],
        )
        self.assertEqual(
            node2.to_html(),
            "<div><span><p>Paragraph text</p></span><p>Normal text<b>Bold text</b><i>italic text</i></p></div>",
            msg="FAILED TEST: node2 does not output expected output",
        )

    def test_errors(self):
        # Test 1: node3 should raise a ValueError because tag property must contain a value
        with self.assertRaises(
            ValueError, msg="FAILED TEST: Able to initalize ParentNode.tag with None"
        ):
            node1 = (ParentNode(None, [LeafNode(None, "Normal text", None)], None),)

        # Test 2: node4 should raise a ValueError because children property must contain a list of ParentNode/LeafNode
        with self.assertRaises(
            ValueError,
            msg="FAILED TEST: Able to initalize ParentNode.children with None",
        ):
            node2 = ParentNode("div", None, None)

        # Test 3: node5 should raise a ValueError because self.children array LeafNode.value is None
        with self.assertRaises(
            ValueError,
            msg="FAILED TEST: Able to initalize Leafnode.value to None inside ParentNode.children list",
        ):
            node3 = ParentNode("div", [LeafNode("b", None, None)], None)


if __name__ == "__main__":
    unittest.main()
