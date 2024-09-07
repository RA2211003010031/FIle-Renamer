import os

def rename_files(folder_path, base_name):
    """
    Renames all files in the given folder with the given base name.

    Args:
        folder_path (str): The path to the folder containing the files to rename.
        base_name (str): The base name to use for renaming the files.

    Returns:
        None
    """
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Rename each file
    for i, file in enumerate(files):
        # Get the file extension
        file_ext = os.path.splitext(file)[1]

        # Create the new file name
        new_name = f"{base_name}-{i+1}{file_ext}"

        # Rename the file
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))

        print(f"Renamed '{file}' to '{new_name}'")

def main():
    folder_path = "C:\\Users\\adars\\OneDrive\\Documents\\ML Project\\train_data"
    base_name = input("Enter the base name: ")

    rename_files(folder_path, base_name)

if __name__ == "__main__":
    main()