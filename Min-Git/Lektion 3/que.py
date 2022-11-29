from linked_list import LinkedList

class Queue(LinkedList):
    def enqueue(self,item):
        """Add item to start of the linked list"""
        self.prepend(item)

    def dequeue(self):
        data = self.tail.data
        self.remove_last_node()
        return data

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.tail is None:
            return None
        
        return self.tail.data

    def size(self):
        pass

if __name__ == '__main__':
    my_queue = Queue()
    print(my_queue)
    print()
