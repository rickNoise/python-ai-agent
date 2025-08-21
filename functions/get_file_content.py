import os

FILE_CHARACTER_LIMIT = 10000

def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
    except Exception as e:
        return f"Error: {e}"
    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    try:
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    except Exception as e:
        return f"Error: {e}"

    # read from the file
    truncation_message = f'[...File "{file_path}" truncated at {FILE_CHARACTER_LIMIT} characters]'
    try:
        with open(full_path, "r") as f:
            file_content_string = f.read(FILE_CHARACTER_LIMIT)
            if len(file_content_string) == FILE_CHARACTER_LIMIT:
                file_content_string += truncation_message
            print(f'Returning file contents from {file_path} at abs path {full_path}...\n\n')
            return file_content_string
    except Exception as e:
        return f"Error: reading file at {full_path}, {e}"
