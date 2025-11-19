def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)

def get_even_numbers(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % 2 == 0]

def safe_divide(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b

def word_frequency(text: str) -> dict[str, int]:
    words = text.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

def max_in_list(numbers: list[int]) -> int:
    if not numbers:
        raise ValueError("List must not be empty")
    return max(numbers)
