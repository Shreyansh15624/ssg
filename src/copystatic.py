import os
import shutil

def copy_static_recursive_trigger(main_dir, directories, public_path):
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    if "public" not in directories or not os.path.exists(public_path):
        os.mkdir(public_path)
    static_path = os.path.join(main_dir, "static")
    if "static" not in directories:
        os.mkdir(static_path)
    return copy_static_recursive(static_path, public_path)

def copy_static_recursive(source, destination):
    source_items = os.listdir(source)
    for source_item in source_items:
        abs_source_item = os.path.join(source, source_item)
        abs_destination_dir = os.path.join(destination, source_item)
        if os.path.isdir(abs_source_item):
            os.mkdir(abs_destination_dir)
            copy_static_recursive(abs_source_item, abs_destination_dir)
        if os.path.isfile(abs_source_item):
            shutil.copy(abs_source_item, destination)