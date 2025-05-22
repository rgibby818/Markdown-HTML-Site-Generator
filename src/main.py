import os
import sys
from move_static_to_docs import move_static_to_docs
from generate_page import generate_pages_recursive, generate_page


def main():

    # Basepath should be set to your github repository name
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]


    cwd = os.getcwd()
    template_file = os.path.join(cwd, "template.html")
    content_folder = os.path.join(cwd, "content")
    docs_folder = os.path.join(cwd, "docs")

    # Delete All items in the public folder (If public does not exist create one)
    # Copy everything from static to public
    move_static_to_docs()

    # Go through the content/ dir in the src/ directory and create html files and put inside of public
    # generate_page(index_file, template_file, public_folder)
    generate_pages_recursive(content_folder, template_file, docs_folder, basepath)


if __name__ == "__main__":
    main()
