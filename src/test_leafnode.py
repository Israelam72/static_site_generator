import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_leafnode_with_props(self):
        test_props = {"href": "https://www.example.com"}
        node = LeafNode("a", "Click here", props=test_props)
        expected = '<a href="https://www.example.com">Click here</a>'
        self.assertEqual(node.to_html(), expected)

    def test_leafnode_without_props(self):
        node = LeafNode("p", "Just a paragraph", props=None)
        expected = "<p>Just a paragraph</p>"
        self.assertEqual(node.to_html(), expected)

    def test_leafnode_no_tag(self):
        node = LeafNode(None, "Raw Text", props=None)
        self.assertEqual(node.to_html(), "Raw Text")


if __name__ == "__main__":
    unittest.main()