class HTMLNode:
    # Initialize an HTML with a tag(<p>), value("This is a paragraph tag"), children(<b>)
    # and properties with key value pairs as dictionaries.
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # TODO
    def to_html(self):
        raise NotImplementedError()

    # Returns a string of each property of an HTML element.
    def props_to_html(self):
        if self.props is not None:
            return (
                f' {" ".join(f'{key}="{value}"' for key, value in self.props.items())}'
            )
        return ""

    # Returns the class of the object and it cooriponding properties.
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    # True if all properties of a object is equal to another.
    def __eq__(self, object):
        if not isinstance(object, HTMLNode):
            return False

        return self.__dict__ == object.__dict__


class LeafNode(HTMLNode):
    # Initalize LeafNode class that inherits from HTMLNode
    # NOTE: "HTMLNode.children" property will be inherited by LeafNode
    # but the value should be None.
    def __init__(self, tag=None, value=None , props=None):
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


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode.tag cannot be None")
        if children is None:
            raise ValueError("ParentNode.children cannot be None")
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        html = f"<{self.tag}{self.props_to_html()}>"

        for children in self.children:
            html += children.to_html()

        html += f"</{self.tag}>"

        return html
