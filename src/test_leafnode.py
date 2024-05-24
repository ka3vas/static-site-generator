import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_props(self):
        node = LeafNode("div", "Hello, world!", {"1": "2", "3": "4"})
        self.assertEqual(node.to_html(), "<div 1=\"2\" 3=\"4\">Hello, world!</div>")

if __name__ == "__main__":
    unittest.main()