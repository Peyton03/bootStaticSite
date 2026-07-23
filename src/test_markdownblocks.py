import unittest
from markdownblocks import markdown_to_blocks, block_to_block_type, MarkdownBlocks   

def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Heading"), MarkdownBlocks.heading)
        self.assertEqual(block_to_block_type("```python\nprint('Hello')\n```"), MarkdownBlocks.code)
        self.assertEqual(block_to_block_type("> This is a quote"), MarkdownBlocks.quote)
        self.assertEqual(block_to_block_type("- List item"), MarkdownBlocks.unordered_list)
        self.assertEqual(block_to_block_type("1. Ordered item"), MarkdownBlocks.ordered_list)
        self.assertEqual(block_to_block_type("This is a paragraph."), MarkdownBlocks.paragraph)

            