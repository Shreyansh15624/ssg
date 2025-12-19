from textnode import BlockType
from convex import block_to_block_type
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

if __name__ == "__main__":
    unittest.main()
        