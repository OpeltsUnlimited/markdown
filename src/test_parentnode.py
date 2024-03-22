import unittest

from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_init1(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", None, None)

    def test_init2(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, [HTMLNode(None,None,None,None)], None)

    def test_init3(self):
        try:
            node = ParentNode("p", [HTMLNode(None,None,None,None)], None)
        except:
            self.fail("myFunc() raised ExceptionType unexpectedly!")

    def test_props_to_html(self):
        input = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            )
        output_ex = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'

        output_is = input.to_html()
        self.assertEqual(output_is, output_ex)