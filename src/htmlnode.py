class HTMLNode:
    def __init__(self, tag, value , children, props):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props
    
    def to_html(self):
        raise NotImplementedError("HTMLNode")
    
    def props_to_html(self):
        output = []
        if self.props:
            for key, value in self.props.items():
                output.append(f"{key}=\"{value}\"")
        return ' '.join(output)