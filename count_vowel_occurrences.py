# To get a coverage report, run:
# uv run pytest --doctest-modules --cov=count_vowel_occurrences --cov-report=html count_vowel_occurrences.py

def count_vowel_occurrences(text: str, vowel: str) -> int:
    """
    Counts the number of times a specific vowel appears in the given text.
    The search is case-insensitive.

    Parameters:
    text (str): The string to search through.
    vowel (str): A single character representing the vowel to count.

    Returns:
    int: The total count of the vowel in the text.

    Raises:
    ValueError: If the 'vowel' argument is not a single character or
                not a valid vowel (a, e, i, o, u).

    Doctests:
    -- Standard Cases --
    >>> count_vowel_occurrences("hello world", "o")
    2

    -- Edge Case: Vowel Not Present --
    >>> count_vowel_occurrences("myth", "y")
    Traceback (most recent call last):
        ...
    ValueError: 'y' is not a valid vowel.
    """
    # Guard clause 1: Ensure vowel is a single character
    if len(vowel) != 1:
        raise ValueError("Vowel must be a single character.")

    # Guard clause 2: Ensure the character is actually a vowel
    if vowel.lower() not in "aeiou":
        raise ValueError(f"'{vowel}' is not a valid vowel.")

    # Standardize inputs to lowercase for case-insensitivity
    text_lower = text.lower()
    vowel_lower = vowel.lower()

    # Count and return
    return text_lower.count(vowel_lower)
