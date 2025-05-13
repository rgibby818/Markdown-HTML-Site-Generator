import os
from move_static_to_public import move_static_to_public
from generate_page import generate_page


def main():
    # Delete All items in the public folder (If public does not exist create one)
    # Copy everything from static to public
    move_static_to_public()
    print(os.getcwd())
    generate_page(
        os.path.join(os.getcwd(), "content/index.md"),
        os.path.join(os.getcwd(), "template.html"),
        os.path.join(os.getcwd(), "public/index.html"),
    )


if __name__ == "__main__":
    main()
