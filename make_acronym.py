# To run doctests, run:
# uv run python3 -m doctest make_acronym.py

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
    words = phrase.split(" ")
    acronym = ""
    for i in range(len(words)):
        current_word = words[i]
        first_letter = current_word[0]
        acronym += first_letter
    return acronym
