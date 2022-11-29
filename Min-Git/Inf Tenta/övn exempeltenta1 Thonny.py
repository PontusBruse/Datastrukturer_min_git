# Exempeltenta
# 1. enkel-länkad lista
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
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
    
    def print_reverse(self):
        if self.head is None:
            print(None)
            
        else:
            print(self.tail.data)
            current_node = self.head
            while current_node.next is not self.tail:
                current_node = self.head.next
                
            self.tail = current_node
            self.print_reverse()

            
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            self.tail= new_node
        
        
Llist = LinkedList()
Llist.append(1)
print(Llist)
Llist.append(2)

Llist.append(3)
print(Llist)
Llist.print_reverse()
print()



#2. Array
def rotate_left(d, arr):
    
    while d >= 1:
        x = arr.pop(0)
        arr.append(x)
        d -= 1
    
    return arr
    
    
print(rotate_left(1, [1,2,3,4,5]))


#3.
    #1. B
    #2. A
    #3. D
    #4. D
    #5. E

#4.
"""
Värdet till vänster '24:an'plockas ut. Våran array delas upp i 2 nya arrayer i saker som är mindre och saker som är större.
20, 19, 21,   24,   26, 31, 25
Sedan tas det vänstraste värderna i de två nya arrayerna, alltså 20 och 26. samma procedur som innan, vi skapar 2 ny arrayer
av en som är större än 20 och en som är mindre än 20. Nu är problemet på denna sida nedbrutet i minsta möjliga delar och alla saker är på plats
till vänster om 24. Vi har nu 19, 20, 21, 24,     26, 31, 25
På högersidan så skapas en array där det som är mindre än 26 samlas och en där det som är större än 26 samlas.
I detta fall är en sak större och en sak mindre, då har vi brutit ner allt i smådelar och sorterat dem. nu sätter vi ihop delarna.
Dett görs från botten, dvs vi börjar med de delar vi delade upp sist.
resultatet blit 19, 20, 21, 24, 25, 26, 31
"""

#5.
"""
Vi går in i mitten av arrayen och jämmför om det värdet är mindre eller större än 26.
Längden av arrayen har värdet 7, alltså vill vi kolla på index 3. detta gör vi mha len(array)//2 (delat med till heltal).
Värdet där är 24 vilket är mindre än 26 som vi söker. Då vet vi att vårat svar finns till höger i arrayen,(eftersom listan är sorterad).
Vi vill nu kolla i mitten av det som finns till höger i arrayen.
Vi gör samma operation som tidigare då hamnar vi på nr 25, vilket igen är mindre än 26 alltså så finns värdet till höger igen.
Vid nästa jämförelse så hamnar vi på rätt värde och då returnerar vi det indexet vi har.0
"""