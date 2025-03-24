def get_book_text(filepath: str) -> str:
    with open(filepath, 'r') as f:
        return f.read()

def count_words(in_string: str) -> int:
    return len(in_string.split())

def main() -> None:
    text = get_book_text('./books/frankenstein.txt')
    num_words = count_words(text)
    print(f'{num_words} words found in the document')

main()
