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
            new_node.append(TextNode(f"{node.text}", node.text_type))
            break
        sections = re.split(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)
        for string in sections:
            for alt, url in matches:
                if alt == string:
                    new_node.append(TextNode(alt, TextType.IMAGES, url))
                    break
                elif url in string:
                    break
                else:
                    if alt == matches[-1][0]:
                        if len(string) != 0:
                            new_node.append(TextNode(string, TextType.NORMAL))
                    continue
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
        new_nodes = []
        for node in old_nodes:
            matches = extract_markdown_links(node.text)
            if len(matches) == 0:
                new_nodes.append(TextNode(f"{node.text}", node.text_type))
                break
            sections = re.split(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)
            for string in sections:
                for text, url in matches:
                    if text == string:
                        new_nodes.append(TextNode(text, TextType.LINKS, url))
                        break
                    elif url in string:
                        break
                    else:
                        if text == matches[-1][0]:
                            if len(string) != 0:
                                new_nodes.append(TextNode(string, TextType.NORMAL))
                        continue
        return new_nodes


