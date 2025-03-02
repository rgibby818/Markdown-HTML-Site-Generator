from src.htmlnode import LeafNode
from enum import Enum


# Supported markdown styles
class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"


class TextNode:

    # Initalize a Textnode with the text(raw text), text_type(TextType Enum), and url(if avaliable)
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # True if a object properties is equal to another objects properties
    def __eq__(self, object):
        if not isinstance(object, TextNode):
            return False

        return self.__dict__ == object.__dict__

    # Returns a string of the class of TextNode object with the values
    # of its properties. 
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):

    # Check if caller provides a TextNode argument
    if not isinstance(text_node, TextNode):
        raise TypeError("Argument must be a TextNode object.")

    # dReturn a LeafNode with the correct HTML tags for each type of TextType
    match text_node.text_type:
        case TextType.NORMAL:
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
