class TextNode:
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"

    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        result = True
        result &= (self.text == other.text)
        result &= (self.text_type == other.text_type)
        result &= (self.url == other.url)
        return result
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    