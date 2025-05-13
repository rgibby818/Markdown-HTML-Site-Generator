import unittest

from split_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_links,
    text_to_textnodes,
)

from textnode import TextNode, TextType


class Test_Split_Markdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is a text with a **bolded** word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is a text with a ", TextType.NORMAL),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with *italic* word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )

        new_nodes = split_nodes_image([node])

        no_image_node = TextNode(
            "This is text with no image",
            TextType.NORMAL,
        )

        new_no_image_node = split_nodes_image([no_image_node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

        self.assertListEqual(
            [
                TextNode("This is text with no image", TextType.NORMAL),
            ],
            new_no_image_node,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://www.link.com) and another [link2](www.link2.com)",
            TextType.NORMAL,
        )
        new_node = split_nodes_links([node])

        no_link_node = TextNode("This is text with no link", TextType.NORMAL)

        new_no_link_node = split_nodes_links([no_link_node])

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("link", TextType.LINKS, "https://www.link.com"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode("link2", TextType.LINKS, "www.link2.com"),
            ],
            new_node,
        )
        self.assertListEqual(
            [
                TextNode("This is text with no link", TextType.NORMAL),
            ],
            new_no_link_node,
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        node = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.NORMAL),
                TextNode(
                    "obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("link", TextType.LINKS, "https://boot.dev"),
            ],
            node,
        )

        text = "**Look** at this image of a cat ![cat](https://image/of/cat.png) "  # <- Trailing space test
        node = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("Look", TextType.BOLD),
                TextNode(" at this image of a cat ", TextType.NORMAL),
                TextNode("cat", TextType.IMAGES, "https://image/of/cat.png"),
                TextNode(" ", TextType.NORMAL),
            ],
            node,
        )


if __name__ == "__main__":
    unittest.main()
