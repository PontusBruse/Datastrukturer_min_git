
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None


    def __str__(self):
        current_node = self.head
        my_str = ''

        while current_node is not None:
            my_str += f'{current_node.data} -> '
            current_node = current_node.next

        my_str += 'None'
        return my_str


if __name__ == '__main__':
    llist = LinkedList()
    print(llist)

    box1 = Node('a')
    llist.head = box1
    print(llist)

    box2 = Node('b')
    box1.next = box2
    print(llist)


    """
    box1 = Box('a')
    box2 = Box('b')
    box1.next = box2

    print(box1)
    box1.next = box2
    print(box1.next)

    box3 = Box('c')
    box2.next = box3

    print(box1.next.next)
    """