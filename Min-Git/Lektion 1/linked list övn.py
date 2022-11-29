class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None


    def count(self):
        node = self.head
        n = 0

        while node is not None:
            n += 1
            node = node.next
        return n


    def sum(self):
        node = self.head
        s = 0

        while node is not None:
            s += node.data
            node = node.next
        return s

    """
    def add_to_end(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        new_node = Node(value)

        current.next = new_node
        """
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node





    def __str__(self):
        current_node = self.head
        my_str = ""

        while current_node is not None:
            my_str += f"{current_node.data} -> "
            current_node = current_node.next

        my_str += "None"
        return my_str


if __name__ == '__main__':
    llist = LinkedList()
    print(llist)

    # box1 = Node(1)
    # llist.head = box1
    llist.append(1)
    print(llist)

    # box2 = Node(2)
    # box1.next = box2
    llist.append(2)
    print(llist)

    # box3 = Node(3)
    # box2.next = box3
    llist.append(3)
    print(llist)



    current_node = llist.head
    # Börja på första noden och gå till next, tills vi kommer till slutet
    while current_node is not None:
        # Skriva ut vad noden innehåller
        print(current_node.data)

        # Gå vidare till nästa nod
        current_node = current_node.next


    print()
    print(f"Antal nodes är: {llist.count()}")
    assert llist.count() == 3
    print()

    print(f'Summan av alla nodes är: {llist.sum()}')

    print()
    # llist.add_to_end(4)
    print(llist)


    llist.append(4)
    print(f"Antal nodes är: {llist.count()}")
    print(f'Summan av alla nodes är: {llist.sum()}')
    print(llist)