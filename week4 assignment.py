def modify_content(content):
   
    return content.upper()


def read_and_modify_file():
    filename = input("Enter the filename to read: ")
    try:        
        with open(filename, "r") as infile:
            content = infile.read()
       
        modified_content = modify_content(content)

        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ File has been modified and saved as '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


read_and_modify_file()
