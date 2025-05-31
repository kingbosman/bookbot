import os
from stats import get_character_count, get_num_words, sorted_count
import sys


def get_book_text(path) -> str:
    with open(path) as f:
        return f.read()


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    if not (os.path.exists(path)):
        print("Book does not exist")
        sys.exit(1)

    book = get_book_text(path)
    words = get_num_words(book)
    letters = sorted_count(get_character_count(book))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for l in letters:
        if not l["char"].isalpha():
            continue
        print(f"{l['char']}: {l['num']}")
    print("============= END ===============")


main()
