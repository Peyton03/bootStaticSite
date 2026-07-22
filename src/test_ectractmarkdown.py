from unittest import TestCase
from extractmarkdown import extract_markdown_links, extract_markdown_images

def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

def test_extract_markdown_links(self):
    matches = extract_markdown_links(
        "This is text with a [link](https://www.boot.dev)"
    )
    self.assertListEqual([("link", "https://www.boot.dev")], matches)   

def test_extract_markdown_links_with_image(self):
    matches = extract_markdown_links(
        "This is text with a [link](https://www.boot.dev) and an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("link", "https://www.boot.dev")], matches)   

def test_extract_markdown_images_with_link(self):
    matches = extract_markdown_images(
        "This is text with a [link](https://www.boot.dev) and an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)       