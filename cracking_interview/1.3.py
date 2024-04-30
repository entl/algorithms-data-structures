#URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space
# at the end to hold the additional characters,and that you are given the "true"
# length of the string. (Note: If implementing in Java,please use a character array
# so that you can perform this operation in place.)

def urlify(s: str) -> str:
    for i in range(len(s)-1, -1, -1):
        if s[i] == " ":
            s = s[:i] + "%20" + s[i + 1:]

    return s

def test_urlify():
    print(urlify(" Mr John Smith "))
    # assert urlify("Mr John Smith") == "Mr%20John%20Smith"
    # assert urlify("Mr John Smith ") == "Mr%20John%20Smith%20"
    # assert urlify(" Mr John Smith") == "%20Mr%20John%20Smith"

if __name__ == "__main__":
    test_urlify()
    print("1.3.py: All tests passed")