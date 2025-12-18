import re
from htmlnode import LeafNode
from textnode import TextNode, TextType

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
    text_list = (split_nodes_delimiter(text_list, "**", TextType.BOLD)) # bold split
    text_list = (split_nodes_delimiter(text_list, "_", TextType.ITALIC)) # itaics split
    text_list = (split_nodes_delimiter(text_list, "`", TextType.CODE)) # code split
    text_list = (split_nodes_image(text_list))
    text_list = (split_nodes_link(text_list))
    return text_list