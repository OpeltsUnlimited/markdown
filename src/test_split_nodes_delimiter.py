import unittest

from textnode import TextNode
from split_nodes_delimiter import split_nodes_delimiter

class Test_split_nodes_delimiter(unittest.TestCase):
    def test_eq(self):
        input = TextNode("This is text with a `code block` word", TextNode.text_type_text)
        expected = [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("code block", TextNode.text_type_code),
                TextNode(" word", TextNode.text_type_text),
                ]

        output = new_nodes = split_nodes_delimiter([input], "`", TextNode.text_type_code)
        self.assertListEqual(output, expected)


if __name__ == "__main__":
    unittest.main()