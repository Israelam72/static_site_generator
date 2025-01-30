class HTLMNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
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