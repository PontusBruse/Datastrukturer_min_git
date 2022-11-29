from övn_deque import Deque

class Stack(Deque):
    def push(self, number):
       self.add_last(number)

    def pop(self):
        value = self.peek()
        self.remove_last()
        return value

    def peek(self):
        return self.peek_last()


    def size(self):
        return Deque().size()

if __name__ == '__main__':
    s = Stack()
    s.push(25)
    s.push(3)
    s.push(4)
    print(s)
    print(s.is_empty())
    # print(stk.self.list)
    s.remove_last()
    print(s.size())
    # print(stk.peek())
    print(s.pop())
    print(s)