import unittest
from htmlnode import HTLMNode

class TestHTMLNode(unittest.TestCase):
    def test_nodesprops(self):
        test = {
            "href": "https://www.google.com",
            "target": "_blank",
            "target2": "_blank2",
        }
        strg = ' href="https://www.google.com" target="_blank" target2="_blank2"'
        node = HTLMNode("<p>", "Israel", props=test)
        node2 = HTLMNode("<a>", "Israel2", props=test)
        self.assertEqual(node.props_to_html(), strg)

if __name__ == "__main__":
    unittest.main()