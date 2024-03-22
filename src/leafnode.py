from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        props = self.props_to_html()
        if not self.tag:
            return f"{self.value}"
        elif props:
            return f"<{self.tag} {props}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

#<p>This is a paragraph of text.</p>
#<a href="https://www.google.com">Click me!</a>
