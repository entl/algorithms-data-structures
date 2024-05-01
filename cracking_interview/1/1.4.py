# Palindrome Permutation: Given a string, write a function to check
# if it is a permutation of a palin­ drome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.
from collections import Counter


def palindrome_permutation(s: str) -> bool:
    s = s.lower().replace(" ", "")
    counter = Counter(s)
    odd_count = 0
    for count in counter.values():
        if count % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False
    return True


def test_palindrome_permutation():
    print(palindrome_permutation("Tact Coa"))
    assert palindrome_permutation("Tact Coa") is True
    assert palindrome_permutation("Tact boa") is False
    assert palindrome_permutation("Tact boa") is False
    assert palindrome_permutation("Tact boa") is False


if __name__ == "__main__":
    test_palindrome_permutation()