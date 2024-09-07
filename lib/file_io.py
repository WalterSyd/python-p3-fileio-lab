def write_file(file_name, file_content):
    #convert file_name to string
    file_name_str = str(file_name)
    #Add a .txt extension
    file_name_with_extension = file_name_str + '.txt'
    #Write to open,file & close file
    with open(file_name_with_extension, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    file_name_str = str(file_name)
    file_name_with_extension = file_name_str + '.txt'
    with open(file_name_with_extension, 'a') as file:
        #
        file.write(append_content)


def read_file(file_name):
    file_name_str = str(file_name)
    file_name_with_extension = file_name_str + '.txt'
    with open(file_name_with_extension, "r") as fyle:
        fyle.content = fyle.read()
    return fyle.content

