from sys import argv, exit
from os import path as osp
from stats import (
    count_words,
    get_character_amounts,
    sort_character_by_amount,
)


def get_book_text(filepath: str) -> str:
    print(f"Analyzing book found at {filepath}")
    with open(filepath, "r") as f:
        return f.read()


def main() -> None:
    print(" BOOKBOT ".center(30, "="))
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    for arg in argv[1:]:
        if osp.exists(arg) and osp.isfile(arg):
            text = get_book_text(arg)
            print(" Word Count ".center(30, "-"))
            num_words = count_words(text)
            print(f"Found {num_words} total words")
            print(" Character Count ".center(30, "-"))
            chars = get_character_amounts(text)
            for chard in sort_character_by_amount(chars):
                print(f"{chard.get('char')}: {chard.get('count')}")


main()
