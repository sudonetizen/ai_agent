import os
from google.genai import types

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


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes given content on found a file by using working directory and file path.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                 type=types.Type.STRING,
                 description="File path that used to write a file in working directory.",
            ),
            "content": types.Schema(
                 type=types.Type.STRING,
                 description="And content for writing on file.",
            ),
        },
        required=["file_path", "content"],
    ),
)
