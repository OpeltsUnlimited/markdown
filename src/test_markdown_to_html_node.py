import unittest

from markdown_to_html_node import markdown_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode

class Test_markdown_to_html_node(unittest.TestCase):
    def test_markdown_to_html_node(self):
        param_list = [
            ("t0", ParentNode("div", [LeafNode("p","t0")]))
              ]
        for param_in, expected in param_list:
            with self.subTest(param_in):
                self.assertEqual(markdown_to_html_node(param_in).to_html(), expected.to_html())

if __name__ == "__main__":
    unittest.main()