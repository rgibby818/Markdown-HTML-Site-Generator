import os
import re
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    print(
        f"Generating page from {from_path} to {dest_path} using tempalte {template_path}\n"
    )

    # Open the from path and extract its title and convert it to html
    from_file = return_file(from_path)
    generated_html = markdown_to_html_node(from_file).to_html()
    title = extract_title(from_file)

    # Open template path and replace the placeholder {{ title }} {{ content }} with the (title) (generated_html)
    html = template_to_html(template_path, title, generated_html)

    # # Write the html to the destition path
    if not os.path.exists(os.path.dirname(dest_path)):
        try:
            os.makedirs(os.path.dirname(dest_path))
        except OSError as Error:
            raise OSError(f"Failed in creating directory: {os.path.dirname(dest_path)}")
    try:
        with open(dest_path, "w") as file:
            file.write(html)
            print(f"Success writing {file.name}")
    except Exception as Error:
        print(f"Error writing file to {dest_path}\n Error: {Error}")


# Open a file and return its content
def return_file(path):
    content = None
    try:
        with open(path, "r") as file:
            content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"file located at {path} not found")
    except Exception as Error:
        print(f"An error occured opening {file} with Error: \n\t{Error}")
    return content


# Returns the template html document with a title and generated html inside the body
def template_to_html(template_path, title, generated_html):
    html = return_file(template_path)
    html = re.sub(r"{{ Title }}", title, html)
    html = re.sub(r"{{ Content }}", generated_html, html)
    return html
