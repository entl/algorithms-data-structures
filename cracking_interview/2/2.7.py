class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return f"{self.val}"


def is_circular(head):
    if not head or not head.next:
        return False

    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def test_is_cycle():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next

    assert is_circular(head) is True

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    assert is_circular(head) is False

if __name__ == "__main__":
    test_is_cycle()
    print("2.7.py: All tests passed")