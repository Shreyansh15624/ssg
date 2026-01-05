from textnode import TextNode, TextType
from copystatic import copy_static_recursive_trigger
from getcontent import generate_page_recursive
import os
import sys
import shutil
TEMPLATE_NAME = "template.html"

def main():
    
    base_path = sys.argv[1] if sys.argv[1] else "/"
    
    # Defining the Project's Main Directory
    main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    directories = os.listdir(main_dir) # Listing its Contents into a List
    # Process shifted from copystatic to follow the DRY Principle
    
    # Locating the Markdown Content Vault
    content_path = os.path.join(main_dir, "content")
    if "content" not in directories or not os.path.exists(content_path):
        raise FileNotFoundError("The content directory is missing.")
    
    # Locating the 'static' Directory
    static_path = os.path.join(main_dir, "static")
    if "static" not in directories or not os.path.exists(static_path):
        raise FileNotFoundError("The static directory is missing.")
    
    # Identifying the public directory & deleting it, if it exists
    public_path = os.path.join(main_dir, "public")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    
    # Created a new docs_path for GitHub Sites Compatibility
    docs_path = os.path.join(main_dir, "docs")
    if os.path.exists(docs_path):
        shutil.rmtree(docs_path)
    
    # Checking for the 'Template' file
    if TEMPLATE_NAME not in directories:
        raise FileNotFoundError(f"The {TEMPLATE_NAME} file is missing.")
    template_path = os.path.join(main_dir, TEMPLATE_NAME)
    
    # Deleting & Recirsively Copying the 'static' directory
    print("Copying static assets...")
    copy_static_recursive_trigger(main_dir, directories, docs_path)
    
    # Invoking the HTML Page Generator
    print("Generating page content...")
    # generate_page_recursive(content_path, template_path, public_path, base_path)
    generate_page_recursive(content_path, template_path, docs_path, base_path)
    
    """
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)
    """
    
    
if __name__=="__main__":
    main()