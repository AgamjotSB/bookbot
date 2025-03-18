def get_num_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict[str, int]:
    characters = {}
    text = text.lower()
    for char in text:
        if char not in characters:
            characters[char] = 0
        characters[char] += 1
    return characters


def sort_characters(characters: dict[str, int]) -> list[dict[str, int]]:
    list_of_dictionaries = []
    for key in characters:
        if key.isalpha():
            list_of_dictionaries.append({"char": key, "count": characters[key]})
    list_of_dictionaries.sort(reverse=True, key=lambda characters: characters["count"])
    return list_of_dictionaries
