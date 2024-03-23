def markdown_to_blocks(markdown):
    output = []
    collect_block = []

    lines = markdown.split('\n')
    for line in lines:
        if not line:
            outline = '\n'.join(collect_block)
            if outline:
                output.append(outline)
            collect_block = []
        else:
            collect_block.append(line)
    outline = '\n'.join(collect_block)
    if outline:
        output.append(outline)
    return output
