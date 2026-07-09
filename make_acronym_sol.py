# To run doctests, run:
# uv run python3 -m doctest make_acronym_sol.py

def make_acronym(phrase: str) -> str:
    """
    Converts a given phrase into an uppercase acronym.
    Words can be separated by one or more spaces.

    Parameters:
    phrase (str): The input text to convert.

    Returns:
    str: The resulting uppercase acronym.

    Doctests (These will FAIL until you fix the bugs!):
    >>> make_acronym("central processing unit")
    'CPU'
    >>> make_acronym("  user   interface  ")
    'UI'
    >>> make_acronym("Hyper  Text Markup Language")
    'HTML'
    >>> make_acronym("")
    ''
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
