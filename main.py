from stats import get_character_count, get_num_words


def get_book_text(path) -> str:
    with open(path) as f:
        return f.read()


def main():
    book = get_book_text("./books/frankenstein.txt")
    words = get_num_words(book)
    letters = get_character_count(book)

    print(f"{words} words found in the document")
    print(letters)


main()
