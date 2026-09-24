import pytest
from ai_core.generator import sanitize_text

def test_sanitize_text_curly_quotes():
    raw = '“Hello World” and ‘Single Quotes’'
    expected = '"Hello World" and \'Single Quotes\''
    assert sanitize_text(raw) == expected

def test_sanitize_text_em_dash_and_spaces():
    raw = 'Term 1—Notice required\u00a0within 10 days'
    cleaned = sanitize_text(raw)
    assert ' - ' in cleaned
    assert '\u00a0' not in cleaned

def test_sanitize_empty_string():
    assert sanitize_text("") == ""
    assert sanitize_text(None) == ""
