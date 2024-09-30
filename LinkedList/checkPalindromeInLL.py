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
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def checkPalindrome(self):
        slow = fast = self.head
        stack = []
        while fast and fast.next:
            stack.append(slow.data)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        while slow:
            if slow.data != stack.pop():
                print("It's not Palindrome")
                return
            slow = slow.next
        print("It's a Palindrome")

def userInput():
        ll = LinkedList()
        n = int(input("Enter total number of elements in Linked List"))
        for i in range(n):
            data = input(f"Enter element {i+1}: ")
            ll.insert_node(data)
        return ll

ll = userInput()
ll.print_list()
ll.checkPalindrome()