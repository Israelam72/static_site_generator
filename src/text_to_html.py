from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
	if not isinstance(text_node.text_type, TextType):
		raise Exception("Value type not permited")
	print("worked")
	
test = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
text_node_to_html_node(test)
