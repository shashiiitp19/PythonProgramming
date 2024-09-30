class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LikedList:
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

ll = LikedList()
ll.insert_node(2)
ll.insert_node(1)
ll.insert_node(8)
ll.insert_node(23)
ll.print_list()
 
