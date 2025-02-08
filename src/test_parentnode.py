import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
	def node_is_equal(self):
		node = ParentNode(
				"p",
					[
							LeafNode("b", "Bold text"),
							LeafNode(None, "Normal text"),
							LeafNode("i", "italic text"),
							LeafNode(None, "Normal text"),
						],
			)
		expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
		self.assertEqual(node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()