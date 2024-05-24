from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        # Return a string representation of the HTMLNode object
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
    # Render a 'leaf' node as an HTML string
    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            # Return raw text if there is no tag
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
