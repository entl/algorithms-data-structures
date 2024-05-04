from collections import deque


class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return f"{self.val}"


def is_list_palindrome(head: ListNode) -> bool:
    stack = deque()
    cur = head

    while cur:
        stack.append(cur.val)
        cur = cur.next

    cur = head
    while cur:
        if cur.val != stack.pop():
            return False
        cur = cur.next

    return True


def test_is_list_palindrome():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)

    assert is_list_palindrome(head) is True

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)

    assert is_list_palindrome(head) is True

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    assert is_list_palindrome(head) is False


if __name__ == "__main__":
    test_is_list_palindrome()
    print("2.6.py: All tests passed")
