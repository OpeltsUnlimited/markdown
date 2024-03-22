from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    output = []
    for node in old_nodes:
        split_node = node.text.split(delimiter)
        for tst, index in zip(split_node,range(0,len(split_node))):
            if index % 2 == 0:
                output.append(TextNode(tst,node.text_type))
            else:
                output.append(TextNode(tst,text_type))
    return output