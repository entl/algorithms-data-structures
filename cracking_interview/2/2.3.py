# Delete Middle Node: Implement an algorithm to delete a node in the middle
# (i.e., any node but the first and last node, not necessarily the exact middle)
# of a singly linked list, given only access to that node.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


def delete_middle_node(head: Node):
    slow = head
    fast = head

    while fast.next.next is not None and fast.next.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    slow.next = slow.next.next


def test_find_middle_node():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    delete_middle_node(head)

    assert head.data == 1
    assert head.next.data == 2
    assert head.next.next.data == 4
    assert head.next.next.next.data == 5


if __name__ == "__main__":
    test_find_middle_node()
    print("2.3.py: All tests passed")
