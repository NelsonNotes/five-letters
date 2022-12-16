from typing import List


def check_word(
    attempt: str, word: str
) -> List[int]:
    attempt_lower: str = attempt.lower()
    word_lower: str = word.lower()
    result: List[int] = [0, 0, 0, 0, 0]
    unguessed = list(word_lower)
    for i, letter in enumerate(attempt_lower, 0):
        if letter == word_lower[i]:
            result[i] = 2
            unguessed.remove(letter)
    for i, letter in enumerate(attempt_lower, 0):
        if result[i] != 2 and letter in unguessed:
            result[i] = 1
            unguessed.remove(letter)

    return result
