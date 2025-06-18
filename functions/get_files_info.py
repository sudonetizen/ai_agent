import os

def get_dir_size(directory):
    #print("dir", directory)
    dir_size = 0
    dir_contents = os.listdir(directory)
    for x in dir_contents:
        if x == "__pycache__": continue
        if os.path.isfile(directory + "/" + x):
            dir_size += os.path.getsize(directory + "/" + x)
        else:
            dir_size += get_dir_size(x)
    return dir_size        


def get_files_info(working_directory, directory=None):
    info = []
    pwd = os.path.abspath(working_directory)
    #print(pwd)
    contents = os.listdir(working_directory)
    #print(contents)
    if directory != "." and directory not in contents: 
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if directory != "." and os.path.isfile(pwd + "/" + directory):
        return f'Error: "{directory}" is not a directory'
    
    if directory == ".": directory = ""
    for i in os.listdir(working_directory + "/" + directory):
        #print(i)
        if os.path.isdir(pwd + "/" + i):
            info.append(f"- {i}: file_size={get_dir_size(pwd + "/" + directory + "/" + i)} bytes, is_dir=True")
        else:
            info.append(f"- {i}: file_size={os.path.getsize(pwd + "/"+ directory + "/" + i)} bytes, is_dir=False")
    return "\n".join(info) 
