# Remove Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
from collections import defaultdict


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


def remove_dups(head: Node) -> Node:
    prev = None
    current = head
    dups = defaultdict(int)

    while current:
        if dups[current.data]:
            prev.next = current.next
        else:
            dups[current.data] += 1
            prev = current

        current = current.next


def test():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(4)

    remove_dups(head)

    assert head.data == 1
    assert head.next.data == 2
    assert head.next.next.data == 4
    assert head.next.next.next.data == 5
    assert head.next.next.next.next == None


if __name__ == "__main__":
    test()
