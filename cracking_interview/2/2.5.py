class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return f"{self.val}"


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy

    carry = 0
    while l1 or l2:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        res = v1 + v2 + carry
        carry = res // 10
        current.next = ListNode(res % 10)

        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry != 0:
        current.next = ListNode(carry)

    return dummy.next


def test_addTwoNumbers():
    head1 = ListNode(2)
    head1.next = ListNode(4)
    head1.next.next = ListNode(3)

    head2 = ListNode(5)
    head2.next = ListNode(6)
    head2.next.next = ListNode(4)

    res = addTwoNumbers(head1, head2)

    assert res.val == 7
    assert res.next.val == 0
    assert res.next.next.val == 8
    assert res.next.next.next == None


if __name__ == "__main__":
    test_addTwoNumbers()
    print("2.5.py: All tests passed")
