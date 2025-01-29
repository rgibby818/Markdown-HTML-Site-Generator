from textnode import TextNode, TextType
from leafnode import LeafNode


# Convert a TextNode to an HTMLNode(LeafNode)
def text_node_to_html_node(text_node):

    # Check if caller provides a TextNode argument
    if not isinstance(text_node, TextNode):
        raise TypeError("Argument must be a TextNode object.")

    # dReturn a LeafNode with the correct HTML tags for each type of TextType
    match text_node.text_type:
        case TextType.NORMALE:
            return LeafNode(value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINKS:
            return LeafNode(
                tag="a", value=text_node.text, props={"href": f"{text_node.url}"}
            )
        case TextType.IMAGES:
            return LeafNode(
                value="",
                tag="img",
                props={"src": f"{text_node.url}", "alt": f"{text_node.text}"},
            )
        case _:
            # TextType was not implemented or of unknown oragin
            raise ValueError("Unknown TextType")

    pass
