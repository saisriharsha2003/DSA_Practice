"""
This single program demonstrates:
1. Creating a Node Class
2. Creating a Linked List CLass
3. Inserting a new node at begining
4. Inserting a new node at the end
5. Inserting a new ndoe in middle
6. Traverse through Linked List
7. Copy / Merge
8. List Comprehension
=================================================
"""

# ------------------------------------------------
# 1. Creating a Node Class
# ------------------------------------------------

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ------------------------------------------------
# 2. Creating a Linked List Classs
# ------------------------------------------------

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # ------------------------------------------------
    # 3. Inserting a new node at the begining
    # ------------------------------------------------
    
    def insert_at_begining(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

        new_node.next = self.head
        self.head = new_node
        self.length += 1


    # ------------------------------------------------
    # 4. Inserting a new node at the end
    # ------------------------------------------------

    def insert_at_end(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return 
        
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    # ------------------------------------------------
    # 5. Inserting a new node at middle
    # ------------------------------------------------

    def insert_at_middle(self, pos, val):
        if pos < 0 or pos > self.length:
            return
        new_node = Node(val)

        if pos == 0:
            self.insert_at_begining(val)
            return
        
        c = 0
        curr = self.head
        while c < pos - 1:
            curr = curr.next
            c += 1

        new_node.next = curr.next
        curr.next = new_node
        self.length += 1

    # ------------------------------------------------
    # 6. Traverse through Linked List
    # ------------------------------------------------
    
    # Using a seprate user defined method
    def display(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
    
    # Using __str__ method
    def __str__(self):
        curr = self.head
        res = ''
        while curr:
            res += (str(curr.val) + ' -> ')
            curr = curr.next
        
        res += 'None'
        return res

# ----------------------------
# Example Usage
# ----------------------------
if __name__ == "__main__":
    # Create initial list: 1 -> 2 -> 3 -> None
    ll = LinkedList()
    new_node = Node(1)
    ll.head = new_node
    new_node = Node(2)
    ll.head.next = new_node
    new_node = Node(3)
    ll.head.next.next = new_node 
    ll.tail = new_node

    print(ll) # 1 -> 2 -> 3 -> None

    ll.display() # 1 -> 2 -> 3 -> None


    # Insertions
    ll.insert_at_begining(0)  
    ll.display() # 0 -> 1 -> 2 -> 3 -> None
    ll.insert_at_end(4)        
    ll.display() # 0 -> 1-> 2 -> 3 -> 4 -> None
    ll.insert_at_middle(2, 99)  # 0 -> 1 -> 99 -> 2 -> 3 -> 4 -> None
    ll.display()