def count_words(in_string: str) -> int:
    return len(in_string.split())


def get_character_amounts(text: str) -> dict:
    output: dict = {}
    for c in text.lower():
        if not output.get(c):
            output[c] = 1
        else:
            output[c] += 1

    return output

def sort_on(d: dict):
    return d.get('count')


def sort_character_by_amount(mapping: dict) -> list[dict]:
    lst = [{"char": key, "count": value} for key, value in mapping.items()]
    return sorted(lst, reverse=True, key=sort_on)
