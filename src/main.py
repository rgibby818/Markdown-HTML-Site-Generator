from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *


def main():
    node2 = ParentNode(
        "div",
        [
            ParentNode("span", [ParentNode("p", [LeafNode(None, "Paragraph text")])]),
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
    print(node2.to_html())


main()
