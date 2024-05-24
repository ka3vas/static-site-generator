from textnode import TextNode
from htmlnode import HTMLNode

def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)
    test = HTMLNode(1,2,3,{"href": "https://www.google.com", "target": "_blank"})
    print(test)



if __name__ == "__main__":
    main()