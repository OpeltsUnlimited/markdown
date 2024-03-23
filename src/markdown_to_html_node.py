from split_blocks import markdown_to_blocks
from block_types import BlockTypes, block_to_block_type
from parentnode import ParentNode
from leafnode import LeafNode

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    collect_children = []
    for block in markdown_blocks:
        type = block_to_block_type(block)
        if type == BlockTypes.block_type_heading:
            lines = block.split("\n")
            header = len(lines[0].split(' ',1)[0])
            collect_children.append(LeafNode(f"h{header}", block))
        elif type == BlockTypes.block_type_code:
            collect_children.append(ParentNode("pre", [ParentNode("code", [LeafNode(None, block.strip("\'\'\'"))])]))
        elif type == BlockTypes.block_type_quote:
            collect_children.append(ParentNode("blockquote", [LeafNode(None, block.strip("\'\'\'"))]))
        elif type == BlockTypes.block_type_unordered_list:
            entrys = []
            for line in block.split("\n"):
                entrys.append(ParentNode("li", [LeafNode(None, line.split(" ",1)[1])]))
            collect_children.append("ul", entrys)
        elif type == BlockTypes.block_type_ordered_list:
            entrys = []
            for line in block.split("\n"):
                entrys.append(ParentNode("li", [LeafNode(None, line.split(" ",1)[1])]))
            collect_children.append("ol", entrys)
        else: # block_type_paragraph
            collect_children.append(LeafNode("p", block))
            pass
    return ParentNode("div", collect_children)