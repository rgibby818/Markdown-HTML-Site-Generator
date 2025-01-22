from htmlnode import HTMLNode


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
