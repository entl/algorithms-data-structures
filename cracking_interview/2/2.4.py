# Partition: Write code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes greater than or equal to x.
# If x is contained within the list, the values of x
# only need to be after the elements less than x (see below).
# The partition element x can appear anywhere in the "right partition";
# it does not need to appear between the left and right partitions.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


def partition(head: Node, x: int):
    left_dummy, right_dummy = Node(), Node()
    left_tail, right_tail = left_dummy, right_dummy

    while head:
        if head.data < x:
            left_tail.next = head
            left_tail = left_tail.next
        else:
            right_tail.next = head
            right_tail = right_tail.next

        head = head.next

    left_tail.next = right_dummy.next
    right_tail.next = None
    return left_dummy.next


def test_partition():
    head = Node(3)
    head.next = Node(5)
    head.next.next = Node(8)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(2)
    head.next.next.next.next.next.next = Node(1)

    partitioned = partition(head, 5)

    assert partitioned.data == 3
    assert partitioned.next.data == 2
    assert partitioned.next.next.data == 1
    assert partitioned.next.next.next.data == 5
    assert partitioned.next.next.next.next.data == 8
    assert partitioned.next.next.next.next.next.data == 5
    assert partitioned.next.next.next.next.next.next.data == 10


if __name__ == "__main__":
    test_partition()
    print("2.4.py: All tests passed")
