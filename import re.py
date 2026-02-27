import re



def test_header_comments(keira 2026-02-12):
    """Test that student included author and date in header comments"""
    try:
        with open("vars_practice.py", encoding="utf-8") as f:
            kids_code = f.read()
    except FileNotFoundError:
        raise AssertionError("Could not find vars_practice.py file. Make sure the file is named correctly.")
    
    # Get first 500 characters to check header
    header = kids_code[:500]
    
    # Check for author comment
    has_author = bool(re.search(r'keira*:', header, re.IGNORECASE))
    assert has_author, "Missing 'author:' in header comments. Please add your name in the header."
    
    # Check for date comment
    has_date = bool(re.search(r 2026-02-12)*:', header, re.IGNORECASE))
    assert has_date, "Missing 'date:' in header comments. Please add the date in the header."
    
    # Check that author is not empty or still the default
    author_match = re.search(r'author\s*:\s*(.+)', header, re.IGNORECASE)
    if author_match:
        author_value = author_match.group(1).strip()
        assert author_value and author_value.lower() not in ['', 'mr. nguyen', 'student name'], \
            "Please fill in your actual name for 'author:' in the header"


def test_vars_practice(capsys, monkeypatch):
    """Test that student used all 7 input values in their story"""
    # Patch the input with random symbols to ensure student used each input
    # in their story
    inputs = ["|", "]", "*", "&", "^", "#", "@"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop())
    import vars_practice

    captured = capsys.readouterr()

    assert "@" in captured.out, "Missing seventh input"
    assert "#" in captured.out, "Missing sixth input"
    assert "^" in captured.out, "Missing fifth input"
    assert "&" in captured.out, "Missing fourth input"
    assert "*" in captured.out, "Missing third input"
    assert "]" in captured.out, "Missing second input"
    assert "|" in captured.out, "Missing first input"


if __name__ == "__main__":
    # This allows running the tests directly
    import pytest
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
    
print(once upon a time there was a kindgom that only wanted to sleep)
print(the (@) was lonely scence everyone was asleep so not one could play)
print(the(#) might look like a villain )