from typing import List, Dict


def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def get_even_numbers(numbers: List[int]) -> List[int]:
    return [n for n in numbers if n % 2 == 0]


def safe_divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def word_frequency(text: str) -> Dict[str, int]:
    words = text.split()
    freq: Dict[str, int] = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


def max_in_list(values: List[int]) -> int:
    if not values:
        raise ValueError("List is empty")
    return max(values)
