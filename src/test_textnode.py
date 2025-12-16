import unittest

from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node1 = TextNode("This is a Link", TextType.LINK, "www.example.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()