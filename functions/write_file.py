import os

def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
    except Exception as e:
        return f"Error: {e}"
    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        if not os.path.exists(os.path.dirname(full_path)):
            os.makedirs(os.path.dirname(full_path))
    except Exception as e:
        return f"Error: checking path or with makedirs, {e}"

    try:
        with open(full_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f"Error: writing to file at {full_path}, {e}"
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'