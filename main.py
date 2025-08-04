def get_book_text(book_path):
    with open(book_path) as f: # open file
        file_contents = f.read() # reads file
    return file_contents

def main():
    print(get_book_text("books/frankenstein.txt"))

main()
