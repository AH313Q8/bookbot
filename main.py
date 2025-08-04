from stats import word_count, letter_count, letter_sort
import sys

def get_book_text(book_path):
    with open(book_path) as f: # open file
        file_contents = f.read() # reads file
    return file_contents

def main():
    book_path = ""

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    file_contents = get_book_text(book_path)
    print("=" * 12 + " BOOKBOT " + "=" * 12)
    print(f"Analyzing book found at {book_path}...")
    print("-" * 11 + " Word Count " + "-" * 11)
    print(f"Found {word_count(file_contents)} total words")
    print("-" * 9 + " Character Count " + "-" * 9)

    letter_dict = (letter_count(file_contents))
    sorted_letters = letter_sort(letter_dict)

    for item in sorted_letters:
        print(f"{item['char']}: {item['num']}")

    print("=" * 12 + " END " + "=" * 12)

main()
