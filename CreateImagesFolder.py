import os

def createImageFolder():
    # Define the name of the new directory
    new_folder_name = "Product_Images"

    # Get the current working directory
    current_dir = os.getcwd()

    # Define the path to the new directory
    new_dir_path = os.path.join(current_dir, new_folder_name)

    # Create the new directory if it doesn't exist already
    if not os.path.exists(new_dir_path):
        os.makedirs(new_dir_path)
