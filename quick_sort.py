def quick_sort(arr, start, end):
    if end <= start:
        return

    pivot = helper(arr, start, end)

    quick_sort(arr, start, pivot - 1)
    quick_sort(arr, pivot + 1, end)


def helper(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])

    i += 1
    (arr[i], arr[end]) = (arr[end], arr[i])

    return i


def test_quick_sort():
    arr = [1, 5, 2, -2, 4, 6, 8, 8, 0, -1, -2]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)


if __name__ == "__main__":
    test_quick_sort()
