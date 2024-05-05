class Stack:
    top = None
    min_val = []

    def __init__(self, data):
        self.data = data
        self.next = None

    def pop(self):
        if self.top is None:
            return None

        item = self.top.data
        if item == self.min_val[-1]:
            self.min_val.pop()

        self.top = self.top.next
        return item

    def push(self, data):
        if not self.min_val or data <= self.min_val[-1]:
            self.min_val.append(data)

        new_item = Stack(data)
        new_item.next = self.top
        self.top = new_item

    def peek(self):
        if self.top is None:
            return None

        return self.top.data

    def is_empty(self):
        return True if not self.top else False

    def get_min(self):
        return self.min_val[-1] if self.min_val else None


def test_stack():
    test = Stack(1)
    test.push(2)
    print(test.get_min())
    test.push(4)
    print(test.get_min())
    test.push(1)
    print(test.get_min())

    test.pop()
    test.pop()
    test.pop()
    print(test.get_min())


if __name__ == "__main__":
    test_stack()