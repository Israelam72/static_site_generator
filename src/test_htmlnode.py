import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    test = {
            "href": "https://www.google.com",
            "target": "_blank",
            "target2": "_blank2",
        }
    strg = ' href="https://www.google.com" target="_blank" target2="_blank2"'

    def test_nodesprops(self):
        node = HTMLNode("<p>", "Israel", props=TestHTMLNode.test)
        self.assertEqual(node.props_to_html(), TestHTMLNode.strg)

    def test_emptyprops(self):
        node = HTMLNode("<p>", "Israel", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_notequal(self):
        node = HTMLNode("<p>", "Israel", props=TestHTMLNode.test)
        self.assertNotEqual(node.tag, node.value)


if __name__ == "__main__":
    unittest.main()