import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        # Testing the specific format defined in your method
        props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            props
        )
        # Your code formats it as: "href:url target=target"
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"',
        )

    def test_values(self):
        # Test that the values set in init are actually stored
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div"
        )
        self.assertEqual(
            node.value,
            "I wish I could read"
        )
        self.assertEqual(
            node.children,
            None
        )
        self.assertEqual(
            node.props,
            None
        )

    def test_repr(self):
        # Test that the string representation is correct
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"primary": "true"}
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(tag=p, value=What a strange world, children=None, props={'primary': 'true'})",
        )

    def test_eq_true(self):
        # Test that two identical nodes are considered equal
        node = HTMLNode("p", "text")
        node2 = HTMLNode("p", "text")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        # Test that different nodes are NOT equal
        node = HTMLNode("p", "text")
        node2 = HTMLNode("a", "text")
        self.assertNotEqual(node, node2)
    
    def test_eq_false_diff_type(self):
        # Test comparing with a different type entirely
        node = HTMLNode("p", "text")
        self.assertNotEqual(node, "some string")
        

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_to_html_no_tag(self):
        # A node without a tag should just return the raw text value
        node = LeafNode(None, "Just raw text.")
        self.assertEqual(node.to_html(), "Just raw text.")

    def test_to_html_with_props(self):
        # Test rendering with HTML attributes (props)
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = LeafNode("a", "Click me!", props)
        self.assertEqual(node.to_html(),'<a href="https://www.google.com" target="_blank">Click me!</a>')

    # This test is crucial! 
    # Logic usually dictates that a LeafNode MUST have a value to be valid.
    def test_to_html_no_value(self):
        node = LeafNode("p", None)
        # We verify that calling to_html() raises a specific error
        # if the value is missing.
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()

