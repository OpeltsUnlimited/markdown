import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links

class Test_extract_markdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        input = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        output_ex = [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")]

        output_is = extract_markdown_images(input)
        self.assertEqual(output_is, output_ex)
    
    def test_extract_markdown_links(self):
        input = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        output_ex = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]

        output_is = extract_markdown_links(input)
        self.assertEqual(output_is, output_ex)

if __name__ == "__main__":
    unittest.main()