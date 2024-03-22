from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text_to_process = node.text
        images = extract_markdown_images(text_to_process)
        for alt, link in images:
            spited = text_to_process.split(f"![{alt}]({link})", 1)
            print("link", link)
            new_nodes.append(TextNode(spited[0], node.text_type, node.url))
            new_nodes.append(TextNode(alt, TextNode.text_type_image,link))
            try:
                text_to_process = spited[1]
            except IndexError:
                text_to_process = None
        if text_to_process:
            new_nodes.append(TextNode(text_to_process, node.text_type))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text_to_process = node.text
        images = extract_markdown_links(text_to_process)
        for alt, link in images:
            spited = text_to_process.split(f"[{alt}]({link})", 1)
            new_nodes.append(TextNode(spited[0], node.text_type, node.url))
            new_nodes.append(TextNode(alt, TextNode.text_type_link,link))
            try:
                text_to_process = spited[1]
            except IndexError:
                text_to_process = None
        if text_to_process:
            new_nodes.append(TextNode(text_to_process, node.text_type, node.url))
    return new_nodes