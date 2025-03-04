# This file provides functions for handling markdown blocks/sections


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
