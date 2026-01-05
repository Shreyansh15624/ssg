import os
import shutil
from convex import markdown_to_html_node



def extract_title(markdown):
    markdown_lines = markdown.splitlines()
    for line in markdown_lines:
        if line.startswith("# "):
            return (line.lstrip("# ").rstrip())
    raise ValueError("No H1 Headings found")

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating Page from '{from_path}' to '{dest_path}' using '{template_path}'.")
    
    # Reading the Markdown Source File
    md_file = open(from_path, 'r') # File Opened
    md_file_content = md_file.read() # Content Read
    md_file.close() # File Closed
    
    # Reading the HTML Template File
    template_file = open(template_path, 'r') # File Opened
    template_file_content = template_file.read() # Content Read
    template_file.close() # File Closed
    
    # Creating the HTMLNode Class Object
    da_node = markdown_to_html_node(md_file_content)
    html_string = da_node.to_html()
    
    # Extracting the Heading as Title
    page_title = str(extract_title(md_file_content))
    
    # Replaing the Title & Content from the 'template.html'
    full_html_string = template_file_content.replace("{{ Title }}", page_title)
    full_html_string = full_html_string.replace("{{ Content }}", html_string)
    
    # Replacing Links to be Deployable on GitHub Links
    full_html_string = full_html_string.replace('href="/', f'href="{base_path}')
    full_html_string = full_html_string.replace('src="/', f'src="{base_path}')
    
    # Deducing the filename
    from_filename = os.path.basename(from_path)
    
    # Swapping the extension from '.md' to '.html'
    dest_filename = from_filename.replace(".md", ".html")
    
    # New file name created
    dest_file_path = os.path.join(dest_path, dest_filename)
    
    # Making sure that the public has the relevant folder structure to the 'dest_file_path'
    # by creating it if it doesn't recursively by in-built function
    if dest_path != "":
        os.makedirs(dest_path, exist_ok=True)
    
    # Writing the newly transformed content to the'.html' destination document
    with open(dest_file_path, 'w') as f:
        f.write(full_html_string)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    for item in os.listdir(dir_path_content):
        file_from_path = os.path.join(dir_path_content, item)
        file_dest_path = os.path.join(dest_dir_path, item)
        
        # If 'item' is a 'sub-directory'
        if os.path.isdir(file_from_path):
            generate_page_recursive(file_from_path, template_path, file_dest_path, base_path)
        
        # If 'item' is a 'markdown file'
        elif not os.path.isdir(file_dest_path):
            generate_page(file_from_path, template_path, dest_dir_path, base_path)