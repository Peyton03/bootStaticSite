def extract_markdown_images(text: str) -> list[str]:
    """
    Extracts all image URLs from the given markdown text.

    Args:
        text (str): The markdown text to extract image URLs from.

    Returns:
        list[str]: A list of image URLs found in the markdown text.
    """
    import re

    # Regular expression to match markdown image syntax ![alt text](image_url)
    image_pattern = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(image_pattern, text)  

def extract_markdown_links(text: str) -> list[str]:
    """
    Extracts all link URLs from the given markdown text.

    Args:
        text (str): The markdown text to extract link URLs from.

    Returns:
        list[str]: A list of link URLs found in the markdown text.
    """
    import re

    # Regular expression to match markdown link syntax [link text](link_url)
    link_pattern = r"\[(.*?)\]\((.*?)\)"
    return re.findall(link_pattern, text)