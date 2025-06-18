import os

def get_file_content(working_directory, file_path):
    wpath = os.path.abspath(working_directory)
    fpath = os.path.join(wpath, file_path)
    if not fpath.startswith(wpath):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(fpath):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    max_chars = 10000
    with open(fpath, "r") as fhandle:
        content = fhandle.read(max_chars)
        if len(content) >= max_chars: content += f'\nFile "{file_path}" truncated at 10000 characters'  
        return content
