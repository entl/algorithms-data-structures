class Stack:
    top = None

    def __init__(self, data):
        self.data = data
        self.next = None

    def pop(self):
        if self.top is None:
            return None

        item = self.top.data
        self.top = self.top.next
        return item

    def push(self, data):
        new_item = Stack(data)
        new_item.next = self.top
        self.top = new_item

    def peek(self):
        if self.top is None:
            return None

        return self.top.data

    def is_empty(self):
        return True if not self.top else False


def test_stack():
    test = Stack(1)
    test.push(2)
    test.push(4)

    print(test.pop())
    print(test.pop())
    print(test.pop())
    print(test.is_empty())


if __name__ == "__main__":
    test_stack()