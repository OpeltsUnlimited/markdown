import unittest

from textnode import TextNode
from split_nodes import split_nodes_image, split_nodes_link

class Test_split_nodes(unittest.TestCase):
    def test_split_nodes_image(self):
        input = node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextNode.text_type_text)
        output_ex = [
            TextNode("This is text with an ", TextNode.text_type_text),
            TextNode("image", TextNode.text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextNode.text_type_text),
            TextNode(
                "second image", TextNode.text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ]

        output_is = split_nodes_image([input])
        self.assertEqual(output_is, output_ex)

    def test_split_nodes_link(self):
        input = node = TextNode(
            "This is text with an [linki](https://i.imgur.com/zjjcJKZ.png) endText",
            TextNode.text_type_text)
        output_ex = [
            TextNode("This is text with an ", TextNode.text_type_text),
            TextNode("linki", TextNode.text_type_link, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" endText", TextNode.text_type_text),
            ]
        
        output_is = split_nodes_link([input])
        self.assertEqual(output_is, output_ex)

if __name__ == "__main__":
    unittest.main()