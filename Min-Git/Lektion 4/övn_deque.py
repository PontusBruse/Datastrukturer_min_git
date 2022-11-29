class Deque:
    def __init__(self):
        self.list = []

    def __str__(self):
        return str(self.list)

    def add_first(self, number):
        self.list.insert(0,number)

    def add_last(self, number):
        self.list.append(number)

    def peek_first(self):
        return self.list[0]

    def peek_last(self):
        return self.list[-1]

    def remove_first(self):
        del(self.list[0])

    def remove_last(self):
        del(self.list[-1])

    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.list)

if __name__ == '__main__':
    deq = Deque()
    deq.add_last(1)
    print(deq)
    print(deq.is_empty())
    print(deq.size())
    deq.remove_last()
    print(deq)
    deq.add_first(1)
    deq.add_first(2)
    deq.add_first(3)
    print(deq)
    deq.remove_first()
    print(deq)
    print(deq.peek_last())