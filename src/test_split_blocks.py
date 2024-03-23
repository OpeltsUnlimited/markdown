import unittest

from split_blocks import markdown_to_blocks

class Test_markdown_to_blocks(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        param_in = "This is **bolded** paragraph\n\
\n\
This is another paragraph with *italic* text and `code` here\n\
This is the same paragraph on a new line\n\
\n\
\n\
\n\
* This is a list\n\
* with items"

        expected = ["This is **bolded** paragraph",
"This is another paragraph with *italic* text and `code` here\n\
This is the same paragraph on a new line",
"* This is a list\n\
* with items"]
        self.assertEqual(markdown_to_blocks(param_in), expected)

    

if __name__ == "__main__":
    unittest.main()