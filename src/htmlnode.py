class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props in (None, ""):
            return ""
        return f"href:{self.props["href"]} target={self.props["target"]}"
        
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return (self.tag == other.tag) and (self.value == other.value) and (self.children == other.children) and (self.props == other.props)
        return False