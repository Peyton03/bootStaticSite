from enum import Enum
class MarkdownBlocks(Enum):
    paragraph = 1
    heading = 2
    code = 3
    quote =4
    unordered_list = 5
    ordered_list = 6
def block_to_block_type(block):
    if block.startswith("#"):
        return MarkdownBlocks.heading
    elif block.startswith("```"):
        return MarkdownBlocks.code
    elif block.startswith(">"):
        return MarkdownBlocks.quote
    elif block.startswith("-") or block.startswith("*"):
        return MarkdownBlocks.unordered_list
    elif block[0].isdigit() and block[1] == ".":
        return MarkdownBlocks.ordered_list
    else:
        return MarkdownBlocks.paragraph
    
def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    blocks = []
    for block in split_markdown:
        strpblock = block.strip()
        if strpblock == "":
            continue
        blocks.append(strpblock)
    return blocks