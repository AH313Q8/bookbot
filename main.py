from stats import word_count, letter_count, letter_sort

def get_book_text(book_path):
    with open(book_path) as f: # open file
        file_contents = f.read() # reads file
    return file_contents

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    print(f"=" * 12 + " BOOKBOT " + "=" * 12)
    print("Analyzing book found at books/frankenstein.txt...")
    print(f"-" * 11 + " Word Count " + "-" * 11)
    print(f"Found {word_count(file_contents)} total words")
    print(f"-" * 9 + " Character Count " + "-" * 9)

    letter_dict = (letter_count(file_contents))
    sorted_letters = letter_sort(letter_dict)

    for item in sorted_letters:
        print(f"{item['char']}: {item['num']}")

    print(f"=" * 12 + " END " + "=" * 12)

main()
