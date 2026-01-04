class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for key, value in self.props.items():
            props_html += f' {key}="{value}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return (self.tag == other.tag) and (self.value == other.value) and (self.children == other.children) and (self.props == other.props)
        return False
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)
    
    def __eq__(self, other):
        if isinstance(other, ParentNode):
            return (self.tag == other.tag) and (self.children == other.children) and (self.props == other.props)
        return False
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is missing")
        if self.children is None:
            raise ValueError("children is missing")
        children_html = "".join(map(lambda x: x.to_html(), self.children))
        return f"<{self.tag}>{children_html}</{self.tag}>"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
        
    def __eq__(self, other):
        if isinstance(other, LeafNode):
            return (self.tag == other.tag) and (self.value == other.value) and (self.props == other.props)
        return False
    
    def to_html(self):
        if self.value is None:
            raise ValueError("value is missing")
        elif not self.tag:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"