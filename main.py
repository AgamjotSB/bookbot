import sys
from stats import count_characters, get_num_words, sort_characters


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")

    book_text = get_book_text(sys.argv[1])

    print("----------- Word Count ----------")
    num_of_words = get_num_words(book_text)
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    char_count = sort_characters(count_characters(book_text))
    for dict in char_count:
        print(f"{dict["char"]}: {dict["count"]}")
    print("============= END ===============")


main()
