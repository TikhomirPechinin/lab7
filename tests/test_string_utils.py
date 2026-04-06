import pytest
from my_library.string_utils import reverse_string, count_vowels, capitalize_words

def test_reverse_string_normal():
    assert reverse_string("hello") == "olleh"

def test_reverse_string_empty():
    assert reverse_string("") == ""

def test_reverse_string_palindrome():
    assert reverse_string("madam") == "madam"

def test_reverse_string_not_string():
    with pytest.raises(TypeError):
        reverse_string(123)

def test_count_vowels_english():
    assert count_vowels("hello") == 2

def test_count_vowels_russian():
    assert count_vowels("привет") == 2

def test_count_vowels_mixed():
    assert count_vowels("Hello World") == 3

def test_count_vowels_empty():
    assert count_vowels("") == 0

def test_count_vowels_no_vowels():
    assert count_vowels("xyz") == 0

def test_capitalize_words_normal():
    assert capitalize_words("hello world") == "Hello World"

def test_capitalize_words_single():
    assert capitalize_words("hello") == "Hello"

def test_capitalize_words_already():
    assert capitalize_words("Hello World") == "Hello World"

def test_capitalize_words_empty():
    assert capitalize_words("") == ""

def test_capitalize_words_not_string():
    with pytest.raises(TypeError):
        capitalize_words(123)