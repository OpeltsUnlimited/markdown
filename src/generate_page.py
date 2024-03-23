from markdown_to_html_node import markdown_to_html_node
import os

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    return ""

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as markdown_file:
        markdown = markdown_file.read()
        content = markdown_to_html_node(markdown).to_html()
        title = extract_title(markdown)

    with open(template_path) as template_file:
        template = template_file.read()
    
    output = template.replace("{{ Title }}", title)
    output = output.replace("{{ Content }}", content)

    with open(dest_path, "w") as dest_file:
        dest_file.write(output)

def generate_pages_recursive(from_path, template_path, dest_path):
    dir_list = os.listdir(from_path)
    for entry in dir_list:
        source_path = os.path.join(from_path,entry)
        target_path = os.path.join(dest_path,entry)
        if os.path.isfile(source_path):
            generate_page(source_path, template_path, os.path.join(dest_path,"index.html"))
        else:
            os.mkdir(target_path)
            generate_pages_recursive(source_path, template_path, target_path)
    