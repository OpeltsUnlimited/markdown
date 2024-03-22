import unittest

from textnode import TextNode
from text_to_textnode import text_to_textnodes

class Test_text_to_textnodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        input = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        
        output_ex = [
            TextNode("This is ", TextNode.text_type_text),
            TextNode("text", TextNode.text_type_bold),
            TextNode(" with an ", TextNode.text_type_text),
            TextNode("italic", TextNode.text_type_italic),
            TextNode(" word and a ", TextNode.text_type_text),
            TextNode("code block", TextNode.text_type_code),
            TextNode(" and an ", TextNode.text_type_text),
            TextNode("image", TextNode.text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", TextNode.text_type_text),
            TextNode("link", TextNode.text_type_link, "https://boot.dev"),
            ]

        output_is = text_to_textnodes(input)

        for a,b in zip(output_ex,output_is):
            print(a, "-", b)

        self.assertEqual(output_is, output_ex)