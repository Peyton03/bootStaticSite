from splitnode import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType
import unittest
class TestSplitNode(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("code block", TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode(" word", TextType.TEXT))


def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

def test_split_links(self): 
    node = TextNode(
        "This is text with a [link](https://www.boot.dev) and another [second link](https://www.example.com)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second link", TextType.LINK, "https://www.example.com"
            ),
        ],
        new_nodes,
    )

class TestTextToTextNodes(unittest.TestCase):
    def test_example(self):
        text = "This is text with a [link](https://www.boot.dev) and an ![image](https://i.imgur.com/zjjcJKZ.png) and a `code block` and **bold text** and _italic text_"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
        ]
        self.assertEqual(result, expected)
        
if __name__ == "__main__":
        unittest.main()