class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def reverseList(self):
        p = None
        c = self.head
        n = c
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        self.head = p

ll = LinkedList()
ll.insert_node(11)
ll.insert_node(3)
ll.insert_node(6)
ll.insert_node(1)
ll.insert_node(2)
ll.print_list()
ll.reverseList()
ll.print_list()  