from utils import (
    count_vowels,
    get_even_numbers,
    safe_divide,
    word_frequency,
    max_in_list
)
def test_count_vowels():
    assert count_vowels("Blue") == 2
    assert count_vowels("sky") == 0

def test_get_even_numbers():
    assert get_even_numbers([1, 2, 3, 4, 6 ,8]) == [2, 4, 6, 8]
    assert get_even_numbers([]) == []

def test_safe_divide():
    assert safe_divide(10, 2) == 5
    assert safe_divide(5, 0) is None

def test_word_frequency():
    assert word_frequency("apple banana apple") == {
        "apple": 2,
        "banana": 1
    }

def test_max_in_list():
    assert max_in_list([1, 5, 3]) == 5
