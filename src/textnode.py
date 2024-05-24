text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"

class TextNode:
    def __init__(self, text, text_type, url=None):
        # Initializing the properties of the class
        # self.text - The text content of the node
        # self.text_type - The type of text this node contains, which is just a string like "bold" or "italic"
        # self.url - The URL of the link or image, if the text is a link. Default to None if nothing is passed in.

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        # Check if all properties are equal
        return (
            self.text == other.text and
            self.text_type == other.text_type and 
            self.url == other.url
        )
            
    def __repr__(self):
        # Return a string representation of the TextNode object
        return f"TextNode({self.text}, {self.text_type}, {self.url})"