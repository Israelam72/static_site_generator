from enum import Enum

class InlineType(Enum):
   NORMAL_TEXT = "normal"
   BOLD_TEXT = "bold"
   ITALIC_TEXT = "italic"
   CODE_TEXT = "code"
   LINKS = "links"
   IMAGES = "images"


class TextNode:
   def __init__(self, text, text_type, url):
      self.text = text
      self.text_type = text_type
      self.url = url

   def __eq__(self, value):
      if (self.text == value.text) and (self.text_type == value.text_type) and (self.url == value.url):
         return True 
      
   def __repr__(self):
      return f"TextNode({self.text}, {self.text_type}, {self.url})"