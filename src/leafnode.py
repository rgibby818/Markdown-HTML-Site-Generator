from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    # Initalize LeafNode class that inherits from HTMLNode
    # NOTE: "HTMLNode.children" property will be inherited by LeafNode
    # but the value should be None.
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode.value cannot be None")
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.tag == None:
            return self.value

        if self.props is None or self.props == {}:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
