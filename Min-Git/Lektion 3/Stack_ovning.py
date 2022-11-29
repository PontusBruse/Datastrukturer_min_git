class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop(-1)

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if len(self.stack) == 0:
            return None

        return self.stack[-1]

    def size(self):
        return len(self.stack)

if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push(3)
    print(my_stack)