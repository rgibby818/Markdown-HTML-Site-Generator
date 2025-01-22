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
