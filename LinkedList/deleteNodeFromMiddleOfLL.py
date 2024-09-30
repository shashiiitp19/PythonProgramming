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

    def delete_mid(self, element):
        mid = self.head
        while mid.next.data is not element:
            mid = mid.next
        mid.next = mid.next.next
    
ll  = LinkedList()
ll.insert_node(3)
ll.insert_node(5)
ll.insert_node(8)
ll.insert_node(1)
ll.insert_node(25)
ll.print_list()
ll.delete_mid(1)
ll.print_list()