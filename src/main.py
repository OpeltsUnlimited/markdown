from textnode import TextNode
from generate_page import generate_page

from copy_static import my_copy

my_copy("static","public");
generate_page("content/index.md", "template.html", "public/index.html")