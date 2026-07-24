from markdownblocks import MarkdownBlocks, block_to_block_type, markdown_to_blocks


class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None ,
        value: str | None ,
        props: dict[str, str] | None = None,
    ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode value cannot be None")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value},{self.props})"
    
class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str | None ,
        children: list["HTMLNode"] | None ,
        props: dict[str, str] | None = None,
    ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("ParentNode tag cannot be None")
        children_html = ""
        if self.children is None:
            raise ValueError("ParentNode children cannot be None")
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

def markdown_to_html_node(markdown:str):
    markdown_blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if block_type == MarkdownBlocks.heading:
            hcounter = 0
            for character in block:
                if character == "#":
                    hcounter += 1
                else:
                    break
            cleaned_text = block[hcounter:].strip()
            children = text_to_children(cleaned_text)
            html_nodes.append(ParentNode(f"h{hcounter}", children))
        elif block_type == MarkdownBlocks.code:
            code_node = LeafNode("code", block[4:-3])
            html_nodes.append(ParentNode("pre", [code_node]))

        elif block_type == MarkdownBlocks.quote:
            spltBlock = block.split("\n")
            cleaned_lines = []
            for line in spltBlock:
                if line.startswith(">"):
                    cleaned_lines.append(line[1:].strip())
            cleaned_text = " ".join(cleaned_lines)
            children = text_to_children(cleaned_text)
            html_nodes.append(ParentNode("blockquote", children))

        elif block_type == MarkdownBlocks.unordered_list:
            items = [item[2:].strip() for item in block.split("\n")]
            list_nodes = []
            for item in items:
                children = text_to_children(item)
                list_nodes.append(ParentNode("li", children))
            html_nodes.append(ParentNode("ul", list_nodes))

            
        elif block_type == MarkdownBlocks.ordered_list:
            items = block.split("\n")
            list_nodes = []
            for item in items:
                parts = item.split(". ", 1)
                cleaned_item = parts[1]
                children = text_to_children(cleaned_item)
                list_nodes.append(ParentNode("li", children))
            html_nodes.append(ParentNode("ol", list_nodes))
            
        elif block_type == MarkdownBlocks.paragraph:
            items = block.split("\n")
            cleaned_text = " ".join([item.strip() for item in items])
            children = text_to_children(cleaned_text)
            html_nodes.append(ParentNode("p", children))

    return ParentNode("div", html_nodes)
def text_to_children(text):
    from splitnode import text_to_textnodes
    from textnode import text_node_to_html_node
    children = []
    for node in text_to_textnodes(text):
        children.append(text_node_to_html_node(node))
    return children
        