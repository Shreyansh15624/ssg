import re
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType, BlockType

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("text_node error")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    final_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final_list.append(node)
            continue
        split_values = node.text.split(delimiter)
        if len(split_values) % 2 == 0:
            raise Exception("unmatched delimiters")
        for i in range(len(split_values)):
            if split_values[i] == "":
                continue
            elif i % 2 != 0:
                res1 = TextNode(split_values[i], text_type)
                final_list.append(res1)
            else:
                res2 = TextNode(split_values[i], TextType.TEXT)
                final_list.append(res2)
    return final_list

def extract_markdown_images(text):
    res = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return res

def extract_markdown_links(text): #(?<!!)
    res = re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return res

def split_nodes_image(old_nodes):
    final_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final_list.append(node)
            continue
        if len(node.text) != 0:
            res1 = extract_markdown_images(node.text)
            if len(res1) == 0:
                final_list.append(node)
                continue
            if len(res1) != 0:
                text = node.text
                for anchor_txt, url in res1:
                    markdown = f"![{anchor_txt}]({url})"
                    before, after = text.split(markdown, 1)
                    if before != "":
                        final_list.append(TextNode(before, TextType.TEXT))
                    final_list.append(TextNode(anchor_txt, TextType.IMAGE, url))
                    text = after
                if text != "":
                    final_list.append(TextNode(text, TextType.TEXT))
    # print(final_list)
    return final_list

def split_nodes_link(old_nodes):
    final_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final_list.append(node)
            continue
        if len(node.text) != 0:
            res2 = extract_markdown_links(node.text)
            if len(res2) == 0:
                final_list.append(node)
                continue
            if len(res2) != 0:
                text = node.text
                for alt_txt, url in res2:
                    markdown = f"[{alt_txt}]({url})"
                    before, after = text.split(markdown, 1)
                    if before != "":
                        final_list.append(TextNode(before, TextType.TEXT))
                    final_list.append(TextNode(alt_txt, TextType.LINK, url))
                    text = after
                if text != "":
                    final_list.append(TextNode(text, TextType.TEXT))
    # print(final_list)
    return final_list

def text_to_textnodes(text):
    text_list = [TextNode(text, TextType.TEXT)]
    text_list = split_nodes_delimiter(text_list, "**", TextType.BOLD) # bold split
    text_list = split_nodes_delimiter(text_list, "_", TextType.ITALIC) # itaics split
    text_list = split_nodes_delimiter(text_list, "`", TextType.CODE) # code split
    text_list = split_nodes_image(text_list)
    text_list = split_nodes_link(text_list)
    return text_list

def markdown_to_blocks(text):
    parts = text.split("\n\n")
    cleaned_blocks = []
    for block in parts:
        block = block.strip()
        if block == "":
            continue
        block = block.strip()
        cleaned_blocks.append(block)
    return cleaned_blocks

def block_to_block_type(block):
    # Case 1: BlockType.HEADING
    if block.startswith("#"):
        hash_count = 0
        i = 0
        while i < len(block) and block[i] == "#":
            hash_count += 1
            i += 1
        if i < len(block) and block[i] == " " and hash_count in range(1, 7):
            return BlockType.HEADING
    # Case 2: BlockType.CODE
    if block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    # Case 3: BlockType.QUOTE
    if block.startswith(">"):
        split_blocks = block.split("\n")
        fact = True
        for block_part in split_blocks: 
            if not block_part.startswith(">"):
                fact = False
                break
        if fact:
            return BlockType.QUOTE
    # Case 4: BlockType.UNORDERED_LIST
    if block.startswith("- "):
        split_blocks = block.split("\n")
        fact = True
        for block_part in split_blocks:
            if not block_part.startswith("- "):
                fact = False
                break
        if fact:
            return BlockType.UNORDERED_LIST
    # Case 5: BlockType.ORDERED_LIST
    if block.startswith("1. "):
        split_blocks = block.split("\n")
        fact = True
        for i in range(len(split_blocks)):
            if not split_blocks[i].startswith(f"{i+1}. "):
                fact = False
                break
        if fact == True:
            return BlockType.ORDERED_LIST
    # Default Case: BlockType.PARAGRAPH
    return BlockType.PARAGRAPH

def text_to_children(text): # The Glue Function, also helps to avoid repitition
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid Code Block")
    text = block[4:-3].strip()
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid Quote Block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return olist_to_html_node(block)
    raise ValueError("Invalid Block Type")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)