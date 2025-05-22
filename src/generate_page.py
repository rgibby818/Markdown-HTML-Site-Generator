import os
import re
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    # If dir_path is a file generate page.
    if not os.path.isdir(dir_path_content):
        return generate_page(dir_path_content, template_path, dest_dir_path, basepath)

    # List content and loop through recursivaly calling until all pages are generated
    files = os.listdir(dir_path_content)
    for file in files:
        file_path = os.path.join(dir_path_content, file)
        destiantion = os.path.join(dest_dir_path, file)
        if os.path.isdir(file_path):
            os.mkdir(destiantion)
            generate_pages_recursive(file_path, template_path, destiantion, basepath)
        else:
            # Source files are .md need to replace with .html for destiantion
            generate_page(
                file_path, template_path, destiantion.split(".")[0] + ".html", basepath
            )


def generate_page(from_path, template_path, dest_path, basepath):
    print(
        f"Generating page from {from_path} to {dest_path} using tempalte {template_path}\n"
    )

    # Open the from path and extract its title and convert it to html
    from_file = return_file(from_path)
    generated_html = markdown_to_html_node(from_file).to_html()
    title = extract_title(from_file)

    # Open template path and replace the placeholder {{ title }} {{ content }} with the (title) (generated_html)
    html = template_to_html(template_path, title, generated_html)
    # Replace all instances of href="/" and src="/" with href="basepath" and src="basepath"
    html = html.replace('href="/', 'href="' + basepath)
    html = html.replace('src="/', 'src="' + basepath)

    # # Write the html to the destition path
    if not os.path.exists(os.path.dirname(dest_path)):
        try:
            os.makedirs(os.path.dirname(dest_path))
        except OSError as Error:
            raise OSError(f"Failed in creating directory: {os.path.dirname(dest_path)}")
    try:
        with open(dest_path, "w") as file:
            file.write(html)
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
    html = html.replace("{{ Title }}", title)
    html =html.replace("{{ Content }}", generated_html)
    return html
