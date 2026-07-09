# Run tests with:
# uv run pytest tests/test_make_acronym.py

def make_acronym(phrase: str) -> str:
    """
    Converts a given phrase into an uppercase acronym.
    Words can be separated by one or more spaces.
    """
    words = phrase.split(" ")
    print(f"words is {words}")
    acronym = ""
    for i in range(len(words)):
        current_word = words[i]
        print(f"current_word is {current_word}")
        first_letter = current_word[0]
        acronym += first_letter
    return acronym
