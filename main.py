from stats import word_count

def get_book_text(book_path):
    with open(book_path) as f: # open file
        file_contents = f.read() # reads file
    return file_contents

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    print(f"{word_count(file_contents)} words found in the document")

main()
