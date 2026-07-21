from textnode import TextNode, TextType
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type == text_type.TEXT:
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