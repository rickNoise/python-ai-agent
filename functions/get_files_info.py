import os

def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, directory))
    except Exception as e:
        return f"Error: {e}"
    
    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    try:
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
    except Exception as e:
        return f"Error: {e}"
    
    dirContentsList = []
    try:
        listdirList = os.listdir(full_path)
    except Exception as e:
        return f"Error: {e}" 

    for item in sorted(listdirList):
        try: 
            item_path = os.path.join(full_path, item)
            dirContentsList.append(f" - {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}")
        except Exception as e:
            return f"Error: {e}"
    
    if directory == ".":
        header = "Result for current directory:"
    else:
        header = f"Result for '{directory}' directory:"
    return header + "\n" + "\n".join(dirContentsList)