# Run tests with:
# uv run pytest tests/test_make_acronym.py

from make_acronym import make_acronym

def test_make_acronym_simple():
    assert make_acronym("central processing unit") == 'CPU'

def test_make_acronym_whitespace():
    assert make_acronym("  user   interface  ") == 'UI'

def test_make_acronym_long():
    assert make_acronym("Hyper  Text Markup Language") == 'HTML'

def test_make_acronym_empty():
    assert make_acronym("") == ''
