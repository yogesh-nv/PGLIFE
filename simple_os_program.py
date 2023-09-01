import os

def list_files_in_directory(path):
    try:
        files = os.listdir(path)
        print(f"Files in directory '{path}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Directory '{path}' not found.")
        
def create_directory(path):
    try:
        os.mkdir(path)
        print(f"Directory '{path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{path}' already exists.")
    except FileNotFoundError:
        print(f"Parent directory for '{path}' not found.")
    except Exception as e:
        print(f"Error occurred while creating '{path}': {e}")

if __name__ == "__main__":
    while True:
        print("\n1. List files in directory")
        print("2. Create a new directory")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            directory_path = input("Enter the directory path: ")
            list_files_in_directory(directory_path)
        elif choice == "2":
            new_directory_path = input("Enter the new directory path: ")
            create_directory(new_directory_path)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
