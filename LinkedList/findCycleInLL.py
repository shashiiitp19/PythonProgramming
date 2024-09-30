class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_data(self, data):
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

    def make_Cycle(self):
        slow = self.head
        fast = self.head
        while fast.next:
            fast = fast.next
        fast.next = slow.next.next

    def detect_Cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("Cycle Found")
                return True
        else:
            print("Cycle Not Found")
            return False

ll = LinkedList()
ll.insert_data(12)
ll.insert_data(1)
ll.insert_data(4)
ll.insert_data(7)
ll.insert_data(9)
ll.print_list()
ll.make_Cycle()
#ll.print_list()
ll.detect_Cycle()

                

