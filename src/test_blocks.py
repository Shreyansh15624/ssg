from textnode import BlockType
from htmlnode import HTMLNode
from convex import block_to_block_type, markdown_to_html_node
import unittest

class TestBlockToBlockType(unittest.TestCase):
    def test_block_heading(self):
        self.assertEqual(block_to_block_type("# This is a heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### This is h6"), BlockType.HEADING)
    
    def test_block_paragraph_heading_failures(self):
        # These look like headings but are invalid, so they should return PARAGRAPH
        self.assertEqual(block_to_block_type("####### Too many hashes"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("#No space"), BlockType.PARAGRAPH)

    def test_block_code(self):
        self.assertEqual(block_to_block_type("```\ncode block\n```"), BlockType.CODE)
        self.assertNotEqual(block_to_block_type("```\ncode block\n``"), BlockType.CODE)

    def test_block_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("> Line 1\n> Line 2"), BlockType.QUOTE)

    def test_block_quote_failure(self):
        # Starts with > but has a bad second line
        self.assertEqual(block_to_block_type("> Valid\nInvalid"), BlockType.PARAGRAPH)

    def test_block_unordered_list(self):
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST)

    def test_block_unordered_list_failure(self):
        # Starts correctly but fails later
        self.assertEqual(block_to_block_type("- Item 1\nItem 2"), BlockType.PARAGRAPH)

    def test_block_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First\n2. Second"), BlockType.ORDERED_LIST)

    def test_block_ordered_list_failure(self):
        # Wrong sequence (1 then 3)
        self.assertEqual(block_to_block_type("1. First\n3. Third"), BlockType.PARAGRAPH)

    def test_block_paragraph(self):
        self.assertEqual(block_to_block_type("Just a normal paragraph."), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraph(self):
        md = """
This is a paragraph
with two lines.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a paragraph with two lines.</p></div>",
        )

    def test_lists(self):
        md = """
- Item 1
- Item 2
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li></ul></div>",
        )

    def test_headings(self):
        md = """
# Header 1

### Header 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Header 1</h1><h3>Header 3</h3></div>",
        )

    def test_code_block(self):
        md = "```\nprint(\"Hello\")\n```"
        
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>print(\"Hello\")</code></pre></div>",
        )


if __name__ == "__main__":
    unittest.main()
        