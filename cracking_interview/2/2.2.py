# Return Kth to Last: Implement an algorithm to
# find the kth to last element of a singly linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


def kth_to_last(head: Node, k: int):
    left = head
    right = head
    right_count = 0

    while right.next is not None:
        if right_count != k:
            right = right.next
            right_count += 1
        else:
            right = right.next
            left = left.next

    return left


def test_kth_to_last():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    assert kth_to_last(head, 2).data == 3


if __name__ == "__main__":
    test_kth_to_last()
    print("2.2.py: All tests passed")