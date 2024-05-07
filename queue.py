class Queue:
    def __init__(self, data=None):
        self.data = data
        self._next = None
        self.__first = None
        self.__last = None

    def add(self, data):
        new_item = Queue(data)

        if self.__last is not None:
            self.__last._next = new_item

        self.__last = new_item
        if self.__first is None:
            self.__first = self.__last

    def remove(self):
        if self.__first is None:
            return None

        item_data = self.__first.data
        self.__first = self.__first._next
        if self.__first is None:
            self.__last = None

        return item_data

    def peek(self):
        if self.__first is None:
            return None

        return self.__first.data

    def is_empty(self):
        return self.__first is None


def test_queue():
    test = Queue()
    test.add(1)
    test.add(2)
    test.add(5)

    assert test.peek() == 1
    assert test.remove() == 1
    assert test.remove() == 2
    assert test.remove() == 5

    assert test.is_empty()


if __name__ == "__main__":
    test_queue()
