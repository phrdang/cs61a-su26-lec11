# Run tests with:
# uv run pytest tests/test_make_acronym.py

def make_acronym(phrase: str) -> str:
    """
    Converts a given phrase into an uppercase acronym.
    Words can be separated by one or more spaces.
    """
    # FIX 1: .split() with no arguments handles multiple spaces
    # and prevents empty strings from slipping into our list.
    words = phrase.split()
    acronym = ""

    for i in range(len(words)):
        current_word = words[i]

        # This is now perfectly safe because current_word will never be empty
        first_letter = current_word[0]
        acronym += first_letter

    # FIX 2: Ensure the entire acronym is forced to uppercase
    return acronym.upper()
