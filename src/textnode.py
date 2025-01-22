from enum import Enum


# Supported markdown styles
class TextType(Enum):
    NORMALE = "normal"
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
