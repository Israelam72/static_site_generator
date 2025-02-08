class HTMLNode:
    def __init__(self, tag=None, value=None, props=None, children=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_dict = self.props.copy()
        strg = "".join(list(map(lambda kv: f' {kv[0]}="{kv[1]}"', props_dict.items())))
        return strg
    
    def __repr__(self):
        return f"{self}"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("Must have a value")
        elif not self.tag:
            return self.value
        else:
            if self.props:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, props=props, children=children)

    def to_html(self):
        if not self.tag:
            raise ValueError("Must have a tag")
        elif len(self.children) == 0:
            raise ValueError("Children argument must have a value")
        
        children_html = "".join(child.to_html() for child in self.children)
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        return f"<{self.tag}>{children_html}</{self.tag}>"
