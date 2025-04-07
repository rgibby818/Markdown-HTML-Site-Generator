# This file contains functions that read  inline markdown text and convert them to a Textnode Object.

import re
from src.textnode import TextNode, TextType
from src.extract_markdown import extract_markdown_images, extract_markdown_links


# Return a list of TextNode that contain delimiter formats.
# Example:
#   "This is **bold** Text"
# Returns:
#   [
#       TextNode("This is", normal, None),
#       TextNode("bold", bold, None),
#       TextNode("Text", normal, None)
#   ]
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.NORMAL))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


# Returns a list of TextNodes that contain markdown image formats.
# Example:
#  "This is text with a image ![an image](image.png)"
# Return:
#   [
#       TextNode("This is atext with a image ", normal, None),
#       TextNode("an image", images, "image.png")
#   ]
def split_nodes_image(old_nodes):
    new_node = []
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        if len(matches) == 0:
            new_node.append(TextNode(f"{node.text}", node.text_type, node.url))
            continue
        sections = re.split(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)
        for string in sections:
            if string != "":
                for text, link in matches:
                    if string == text:
                        new_node.append(TextNode(string, TextType.IMAGES, link))
                        break
                    elif string == link:
                        break
                    elif text == matches[-1][0]:
                        new_node.append(TextNode(string, TextType.NORMAL))
                        break
    return new_node


# Returns a list of TextNodes that contain markdown link formats.
# Example:
#   "This is a [a link](https://www.link.com) to a website"
# Returns:
#   [
#       TextNode("This is a ", normal, None),
#       TextNode("a link", links, "https://www.link.com"),
#       TextNode("to a website", normal, none)
#   ]
def split_nodes_links(old_nodes):
    new_node = []
    for node in old_nodes:
        matches = extract_markdown_links(node.text)
        if len(matches) == 0:
            new_node.append(TextNode(f"{node.text}", node.text_type, node.url))
            continue
        sections = re.split(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)
        for string in sections:
            if string != "":
                for text, link in matches:
                    if string == text:
                        new_node.append(TextNode(string, TextType.LINKS, link))
                        break
                    elif string == link:
                        break
                    elif text == matches[-1][0]:
                        new_node.append(TextNode(string, TextType.NORMAL))
                        break
    return new_node


# Returns a list of all inline markdown formats
# Example:
# "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
# Returns:
# #   [
#     TextNode("This is ", TextType.TEXT),
#     TextNode("text", TextType.BOLD),
#     TextNode(" with an ", TextType.TEXT),
#     TextNode("italic", TextType.ITALIC),
#     TextNode(" word and a ", TextType.TEXT),
#     TextNode("code block", TextType.CODE),
#     TextNode(" and an ", TextType.TEXT),
#     TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
#     TextNode(" and a ", TextType.TEXT),
#     TextNode("link", TextType.LINK, "https://boot.dev"),
# ]
def text_to_textnode(text):
    new_node = split_nodes_delimiter(
        [
            TextNode(text, TextType.NORMAL),
        ],
        "**",
        TextType.BOLD,
    )
    new_node = split_nodes_delimiter(new_node, "__", TextType.BOLD)
    new_node = split_nodes_delimiter(new_node, "*", TextType.ITALIC)
    new_node = split_nodes_delimiter(new_node, "_", TextType.ITALIC)
    new_node = split_nodes_delimiter(new_node, "`", TextType.CODE)
    new_node = split_nodes_image(new_node)
    new_node = split_nodes_links(new_node)
    return new_node
