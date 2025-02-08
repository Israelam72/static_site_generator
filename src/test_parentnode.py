import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
	def test_node_is_equal(self):
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

	def test_missing_tag_raises_value_error(self):
		with self.assertRaises(ValueError) as context:
			ParentNode(None, []).to_html()
		self.assertEqual(str(context.exception), "Must have a tag")

	def test_missing_children_raises_value_error(self):
		with self.assertRaises(ValueError) as context:
			ParentNode("p", None).to_html()
		self.assertEqual(str(context.exception), "Children argument must have a value")

	def test_invalid_children_raises_value_error(self):
		with self.assertRaises(ValueError) as context:
			ParentNode("p", ["not-an-node"]).to_html()
		self.assertEqual(str(context.exception), "All children must be instances of HTMLNode")

if __name__ == "__main__":
    unittest.main()