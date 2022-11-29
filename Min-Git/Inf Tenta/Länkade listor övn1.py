class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __str__(self):
        current_node = self.head
        my_str= ""
        
        while current_node is not None:
            my_str += f"{current_node.data} -> "
            current_node = current_node.next
            
        my_str += " None"
            
        return my_str
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert(self, data, after_data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            current_node = self.head
            while current_node.data != after_data:
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            


if __name__ == '__main__':
    llist = LinkedList()
    print(llist)
    
    n1 = Node(1)
    llist.head = n1
    print(llist)
    
    n2 = Node(2)
    n1.next = n2
    print(llist)
    
    llist2 = LinkedList()
    print(llist2)
    
    llist2.append("a")
    print(llist2)
    
    llist2.append("b")
    llist2.append("c")
    llist2.append("d")
    llist2.append("e")
    print(llist2)
    
    llist2.prepend("ö")
    print(llist2)
    
    llist2.insert("x", "d")
    print(llist2)

    