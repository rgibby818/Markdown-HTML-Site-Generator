import os
from move_static_to_public import move_static_to_public
from generate_page import generate_pages_recursive, generate_page


def main():

    cwd = os.getcwd()
    template_file = os.path.join(cwd, "template.html")
    content_folder = os.path.join(cwd, "content")
    public_folder = os.path.join(cwd, "public")

    # Delete All items in the public folder (If public does not exist create one)
    # Copy everything from static to public
    move_static_to_public()

    # Go through the content/ dir in the src/ directory and create html files and put inside of public
    # generate_page(index_file, template_file, public_folder)
    generate_pages_recursive(content_folder, template_file, public_folder)


if __name__ == "__main__":
    main()
