import unittest

from leafnode import LeafNode
from textnode import TextNode
from text_node_to_html_node import text_node_to_html_node

class TestTextToLeave(unittest.TestCase):
    def test_to_html(self):
        param_list = [
             (TextNode("text", TextNode.text_type_text), 
              LeafNode("", "text")),
             (TextNode("bold", TextNode.text_type_bold), 
              LeafNode("b", "bold")),
             (TextNode("italic", TextNode.text_type_italic), 
              LeafNode("i", "italic")),
             (TextNode("code", TextNode.text_type_code), 
              LeafNode("code", "code")),
             (TextNode("achorText", TextNode.text_type_link, "url:/a"), 
              LeafNode("a", "achorText", {"href":"url:/a"})),
             (TextNode("alt", TextNode.text_type_image, "url:/b"), 
              LeafNode("img", "", {"src":"url:/b" ,"alt":"alt"})),
              ]
        for param_in, expected in param_list:
            with self.subTest(expected):
                self.assertEqual(text_node_to_html_node(param_in).to_html(), expected.to_html())

if __name__ == "__main__":
    unittest.main()