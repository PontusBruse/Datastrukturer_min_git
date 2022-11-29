
class Node:
    def __init__(self, data):
        """ Store the data, and set next to None"""
        self.data = data
        self.next = None

    def __str__(self):
        """ Return a string representation of the data """
        return str(self.data)


class Storage:
    def __init__(self):
        """ Creates an empty Storage class. Sets head to None. """
        self.head = None

    def push(self, data):
        """ Create a Node to hold the data, then put it at the head of the list. """
        new_node = Node(data)

        # Update the new_node to the new head node
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """ Remove the head Node and return its data. """
        # If list is empty, return None
        if self.head is None:
            return None

        # Create a temporary value that points to the head
        current = self.head
        self.head = current.next
        return current.data

    def peek(self):
        """ Return the data from the head Node, without removing it. """
        return self.head.data

    def isempty(self):
        """ Return True if the list is empty, otherwise False """
        if  self.head == None:
            return True
        else:
            return False


if __name__== '__main__':
    store = Storage()

    store.push('Hej')
    print(store.isempty())
    print(store.peek())
    print(store.pop())
    print(store.isempty())

