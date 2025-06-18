import os

def write_file(working_directory, file_path, content):
    wpath = os.path.abspath(working_directory)
    fpath = os.path.join(wpath, file_path)
    if not fpath.startswith(wpath):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    fp_parts = fpath.split("/")
    fp_ready = "/".join(fp_parts[:-1])
    if not os.path.exists(fp_ready):
        os.makedirs(fp_ready)

    with open(fpath, "w") as fhandle:
        fhandle.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
