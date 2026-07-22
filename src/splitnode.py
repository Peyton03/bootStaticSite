from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_images, extract_markdown_links
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError("invalid markdown: formatted section not closed")
            for i in range(len(parts)):
                if parts[i] == "":
                    continue  # skip empty pieces
                if i % 2 == 0:
                    new_nodes.append(TextNode(parts[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(parts[i], text_type))

        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            images = extract_markdown_images(node.text)
            print(images)
            remaining_text = node.text
            for image_text, url in images:
                full_image = f"![{image_text}]({url})"
                before, after = remaining_text.split(full_image, 1)
                if before:
                    new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(image_text, TextType.IMAGE, url))
                remaining_text = after
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))

        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            links = extract_markdown_links(node.text)
            print(links)
            remaining_text = node.text
            for link_text, url in links:
                full_link = f"[{link_text}]({url})"
                before, after = remaining_text.split(full_link, 1)
                if before:
                    new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINK, url))
                remaining_text = after
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
            

        else:
            new_nodes.append(node)
    return new_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    node = [TextNode(text, TextType.TEXT)]
    node = split_nodes_delimiter(node, "`", TextType.CODE)
    node = split_nodes_delimiter(node, "**", TextType.BOLD)
    node = split_nodes_delimiter(node, "_", TextType.ITALIC)
    node = split_nodes_image(node)
    node = split_nodes_link(node)
    return node