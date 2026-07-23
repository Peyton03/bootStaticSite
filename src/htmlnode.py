from markdownblocks import MarkdownBlocks, block_to_block_type
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

def markdown_to_html_node(markdown_blocks: list[str]) -> list[HTMLNode]:
    html_nodes = []
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if block_type == MarkdownBlocks.heading:
            html_nodes.append(LeafNode("h1", block[2:].strip()))
        elif block_type == MarkdownBlocks.code:
            html_nodes.append(LeafNode("pre", block.strip()))
        elif block_type == MarkdownBlocks.quote:
            html_nodes.append(LeafNode("blockquote", block[2:].strip()))
        elif block_type == MarkdownBlocks.unordered_list:
            items = [item[2:].strip() for item in block.split("\n")]
            html_nodes.append(ParentNode("ul", [LeafNode("li", item) for item in items]))
        elif block_type == MarkdownBlocks.ordered_list:
            items = [item[3:].strip() for item in block.split("\n")]
            html_nodes.append(ParentNode("ol", [LeafNode("li", item) for item in items]))
        elif block_type == MarkdownBlocks.paragraph:
            html_nodes.append(LeafNode("p", block.strip()))
    return html_nodes