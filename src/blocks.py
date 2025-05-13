# This file provides functions for handling markdown blocks/sections


from enum import Enum
from split_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_links


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


# Returns a BlockType Enum of a block of Markdown.
# Example:
#   # This is a Heading
# Returns:
#   BlockType.Heading
def block_to_block_type(block):
    headings = ["######", "#####", "####", "###", "##", "#"]
    split_block = block.strip().split("\n")

    if any(block.startswith(heading + " ") for heading in headings):
        return BlockType.HEADING
    if split_block[0].startswith("```") and split_block[-1].endswith("```"):
        return BlockType.CODE
    if len(list(filter(lambda line: line.startswith(">"), split_block))) == len(
        split_block
    ):
        return BlockType.QUOTE
    if len(list(filter(lambda line: line.startswith("-" + " "), split_block))) == len(
        split_block
    ):
        return BlockType.UNORDERED_LIST
    if split_block[0].startswith("1. "):
        i = 1
        for line in split_block:
            if not line.startswith(f"{i}. "):
                break
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


# Takes a raw markdown file and breaks it up into sections
# Example:
# """
# # This is a heading

# This is a paragraph of text. It has some **bold** and _italic_ words inside of it.


# - This is the first list item in a list block
# - This is a list item
# - This is another list item
# """
# Return:
# [
#     "# This is a heading",
#     "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
#     "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
# ]
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    parsed_blocks = []
    for block in blocks:
        if block == "":
            continue
        parsed_blocks.append(block.strip())
    return parsed_blocks
