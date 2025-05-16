import os
from shutil import copy, rmtree


def move_static_to_public():
    public_folder = os.path.join(os.getcwd(), "public")
    static_folder = os.path.join(os.getcwd(), "static")

    # delete everything in the public folder
    if_folder(public_folder, create_folder=True)
    delete_files_in_path(public_folder)

    # Copy items from the static folder into the public folder

    if if_folder(static_folder):
        copy_files(static_folder, public_folder)


# Check if a path exist if create_folder is set to True it will create that folder
def if_folder(path, create_folder=False):

    if not os.path.exists(path):
        if create_folder:
            os.makedirs(path)
            return True
        else:
            raise ValueError("Directory does not exist")
    return True


# Delete every file inside a path
def delete_files_in_path(path):
    if not os.path.exists(path):
        raise ValueError("Directory does not exist")
    items = os.listdir(path)
    for item in items:
        try:
            item_path = os.path.join(path, item)

            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                rmtree(item_path)
            else:
                raise OSError("Item is not a file or a folder")

        except OSError as error:
            print(f"Error Deleting {os.path.join(path, item)}\n Error: {error}")


#
def copy_files(copy_path, paste_path):
    items = os.listdir(copy_path)
    for item in items:
        item_path = os.path.join(copy_path, item)
        if os.path.isfile(item_path):
            copy(item_path, paste_path)
        if os.path.isdir(item_path):
            paste_path_subfolder = os.path.join(paste_path, item)
            os.mkdir(os.path.join(paste_path, item))
            copy_files(item_path, paste_path_subfolder)
