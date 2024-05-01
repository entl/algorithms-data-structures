# One Away: There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check
# if they are one edit (or zero edits) away.

def one_away(s1: str, s2: str) -> bool:
    if len(s1) == len(s2):
        return one_replace_away(s1, s2)

    if len(s1) + 1 == len(s2):
        return one_insert_away(s1, s2)

    if len(s1) - 1 == len(s2):
        return one_insert_away(s2, s1)

    return False


def one_replace_away(s1: str, s2: str) -> bool:
    found_diff = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if found_diff:
                return False
            found_diff = True
    return True


def one_insert_away(s1: str, s2: str) -> bool:
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if i != j:
                return False
            j += 1
        else:
            i += 1
            j += 1
    return True


def test_edit():
    assert one_away("pale", "ple") is True
    assert one_away("pales", "pale") is True
    assert one_away("pale", "bale") is True
    assert one_away("pale", "bake") is False


if __name__ == "__main__":
    test_edit()
