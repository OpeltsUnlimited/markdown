from textnode import TextNode
from generate_page import generate_pages_recursive

from copy_static import my_copy

my_copy("static","public");
generate_pages_recursive("content/", "template.html", "public/")