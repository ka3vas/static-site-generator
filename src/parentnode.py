from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        # Return a string representation of the ParentNode object
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        
        string = ""
        for child in self.children:
            string += child.to_html()
        
        return f"<{self.tag}>{string}</{self.tag}>"
