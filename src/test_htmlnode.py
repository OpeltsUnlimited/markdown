import unittest

from htmlnode import HTMLNode
class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        input = {"href": "https://www.google.com", "target": "_blank"}
        output_ex = 'href="https://www.google.com" target="_blank"'

        node = HTMLNode(None, None, None, input)
        output_is = node.props_to_html()
        self.assertEqual(output_is, output_ex)
    
    def test_to_html(self):
        node = HTMLNode(None, None, None, None)
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()