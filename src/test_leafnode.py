import unittest

from leafnode import LeafNode
class TestTextNode(unittest.TestCase):
    
    def test_to_html(self):
        param_list = [
             (LeafNode("p", "This is a paragraph of text."), 
              '<p>This is a paragraph of text.</p>'),
             (LeafNode("a", "Click me!", {"href": "https://www.google.com"}), 
              '<a href="https://www.google.com">Click me!</a>')
        ]
        for param_in, expected in param_list:
            with self.subTest(expected):
                self.assertEqual(param_in.to_html(), expected)

    

if __name__ == "__main__":
    unittest.main()