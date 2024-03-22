from textnode import TextNode
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    working = [TextNode(text, TextNode.text_type_text)]
    working = split_nodes_delimiter(working, '**',TextNode.text_type_bold)
    working = split_nodes_delimiter(working, '*',TextNode.text_type_italic)
    working = split_nodes_delimiter(working, '`',TextNode.text_type_code)
    working = split_nodes_image(working)
    working = split_nodes_link(working)
    return working


    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"
