from leafnode import LeafNode
from textnode import TextNode

def text_node_to_html_node(text_node):
    translationFunctions = {
        TextNode.text_type_text: lambda text_node : LeafNode("", text_node.text),
        TextNode.text_type_bold: lambda text_node : LeafNode("b", text_node.text),
        TextNode.text_type_italic: lambda text_node : LeafNode("i", text_node.text),
        TextNode.text_type_code: lambda text_node : LeafNode("code", text_node.text),
        TextNode.text_type_link: lambda text_node : LeafNode("a", text_node.text, {"href":text_node.url}),
        TextNode.text_type_image: lambda text_node : LeafNode("img", "", {"src":text_node.url ,"alt":text_node.text}),

    }
    if text_node.text_type in translationFunctions:
        f = translationFunctions[text_node.text_type]
        return f(text_node)
    else:
        raise Exception()