# Read the md file, read its contents, return the contents
# Ignore the empty newlines, existing strig end \n
# Apporach 1: Use readline instead of readlines, and solve the problem
def read_markdown(file_path):
    with open(file_path, "r") as md_file:
        contents = md_file.readlines()
        return contents
    
