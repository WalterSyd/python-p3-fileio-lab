def write_file(file_name, file_content):
    #convert file_name to string
    file_name_str = str(file_name)
    #Add a .txt extension
    file_name_with_extension = file_name_str + '.txt'
    with open(file_name_with_extension, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    pass

def read_file(file_name):
    pass
