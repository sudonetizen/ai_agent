import os
import subprocess

def run_python_file(working_directory, file_path):
    wpath = os.path.abspath(working_directory)
    fpath = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not fpath.startswith(wpath):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    fp_parts = fpath.split("/")
    fp_ready = "/".join(fp_parts[:-1])

    if not os.path.exists(fpath):
        return f'Error: File "{file_path}" not found.'
   
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    text = ""
    try:
        result = subprocess.run(
            ["python3", f"{fp_parts[-1]}"],  
            cwd=fp_ready, 
            timeout=30, 
            capture_output=True, 
            text=True
        )
        
        if result.stdout:
            text += f"STDOUT: {result.stdout.strip()}\n"
        else:
            text += "No output produced\n"
        if result.stderr:
            text += f"STDERR: {result.stderr.strip()}\n"
        if result.returncode != 0:
            text += f"Process exited with code {result.returncode}"

    except subprocess.CalledProcessError as e:
        return f"Error: executing Python file: {e}"
        
    return text 
