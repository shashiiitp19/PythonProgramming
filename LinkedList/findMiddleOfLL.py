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

    def findMiddle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow:
            print(slow.data)
        else:
            print("None")
    
    
ll = LinkedList()
ll.insert_node(19)
ll.insert_node(3)
ll.insert_node(11)
ll.insert_node(9)
ll.insert_node(12)
ll.insert_node(7)
ll.insert_node(5)
ll.print_list()
ll.findMiddle()



