import unittest

from htmlnode import HTMLNode


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
            "href:https://www.google.com target=_blank",
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


if __name__ == "__main__":
    unittest.main()

