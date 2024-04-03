"""Recursive_reverse"""


def recursive_reverse(words: str):
    """Recursive_reverse"""
    n = len(words)
    if n == 0:
        return words
    else:
        return words[n - 1] + recursive_reverse(words[:n-1])


print(recursive_reverse("Hello, world"))
