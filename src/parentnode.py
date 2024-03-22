from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        if not tag:
            raise ValueError("tag missing")
        if not children:
            raise ValueError("no children")
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        inner = []
        for child in self.children:
            inner.append(child.to_html())
        inner = ''.join(inner)
        props = self.props_to_html()
        if props:
            return f"<{self.tag} {props}>{inner}</{self.tag}>"
        else:
            return f"<{self.tag}>{inner}</{self.tag}>"