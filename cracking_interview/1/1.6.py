# String Compression:
# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3.
# If the "compressed" string would not become smaller than the original string,
# your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).

def compression(string: str) -> str:
    compressed = []
    count = 0
    for i in range(len(string)):
        count += 1
        if i + 1 >= len(string) or string[i] != string[i + 1]:
            compressed.append(string[i])
            compressed.append(str(count))
            count = 0
    return "".join(compressed) if len(compressed) < len(string) else string


def test_compression():
    assert compression("aabcccccaaa") == "a2b1c5a3"


if __name__ == "__main__":
    test_compression()
    print("1.6.py: All tests passed")
