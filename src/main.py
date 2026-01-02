from textnode import TextNode, TextType
from copystatic import copy_recursive_trigger

def main():
    
    copy_recursive_trigger()
    
    """
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)
    """
if __name__=="__main__":
    main()