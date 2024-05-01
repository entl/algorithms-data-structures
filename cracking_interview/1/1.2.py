# Check Permutation: Given two strings,
# write a method to decide if one is a permutation of the other.

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)

