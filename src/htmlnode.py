class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # Initializing the properties of the class
        # tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        # value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        # children - A list of HTMLNode objects representing the children of this node
        # props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        # Return a string representation of the HTMLNode object
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        # Child classes will override this method to render themselves as HTML
        raise NotImplementedError("NotImplementedError!")
    
    def props_to_html(self):
        # Return a string that represents the HTML attributes of the node.
        # input: {"href": "https://www.google.com", "target": "_blank"}
        # output: href="https://www.google.com" target="_blank"
        string = ""

        for prop in self.props:
            string += f" {prop}=\"{self.props[prop]}\""

        return string

# Test props_to_html method
test = HTMLNode(1,2,3,{"href": "https://www.google.com", "target": "_blank"}).props_to_html()
print(test)