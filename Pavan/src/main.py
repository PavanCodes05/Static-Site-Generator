from parser import read_markdown

def main():
    file_path = r"markdowns\sample.md"
    
    md_contents = read_markdown(file_path)
    modified_contents = []

    for content in md_contents:
        if content == "\n":
            continue
        modified_contents.append(content.rstrip())


main()