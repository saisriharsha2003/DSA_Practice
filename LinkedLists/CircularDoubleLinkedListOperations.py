class Node:
    def __init__(self, val):
        # Initialize a node with a value and two pointers (prev and next).
        self.val = val
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:

    def __init__(self, values=None):
        # Initialize an empty Circular Doubly Linked List and optionally populate it with values.
        self.head = None

        if values:
            for val in values:
                self.insert_at_end(val)

    # -----------------------------------
    # Insert at Beginning
    # -----------------------------------

    def insert_at_beginning(self, val):
        # Insert a new node at the beginning of the circular doubly linked list.
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.head.next = new_node
            self.head.prev = new_node
            return
        
        tail = self.head.prev
        new_node.next = self.head
        self.head.prev = new_node
        new_node.prev = tail
        tail.next = new_node
        self.head = new_node

    # -----------------------------------
    # Insert at End
    # -----------------------------------

    def insert_at_end(self, val):
        # Insert a new node at the end of the circular doubly linked list.
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.head.next = new_node
            self.head.prev = new_node
            return

        tail = self.head.prev
        new_node.prev = tail
        self.head.prev = new_node
        tail.next = new_node
        new_node.next = self.head

    # -----------------------------------
    # Insert at Position
    # -----------------------------------

    def insert_at_middle(self, pos, val):
        # Insert a new node at the specified position if the position is valid.
        new_node = Node(val)
        if self.head is None:
            if pos == 0:
                self.head = new_node
                self.head.next = new_node
                self.head.prev = new_node
                return
            else:
                return
        
        n = len(self)
        if (pos < 0) or (pos > n):
            return
        
        if pos == 0:
            return self.insert_at_beginning(val)
        
        if pos == n:
            return self.insert_at_end(val)
        
        c = 0
        curr = self.head
        while c < pos - 1:
            curr = curr.next
            c += 1
        
        new_node.next = curr.next
        curr.next.prev = new_node
        curr.next = new_node
        new_node.prev = curr


    # -----------------------------------
    # Insert Before Value
    # -----------------------------------

    def insert_before(self, target, val):
        # Insert a new node immediately before the first occurrence of the target value.
        
        if not self.head:
            return
        
        if self.head.val == target:
            return self.insert_at_beginning(val)
        
        tail = self.head.prev
        new_node = Node(val)
        curr = self.head
        
        while curr.next.val != target and curr.next != self.head:
            curr = curr.next
        
        if curr == tail:
            return
        
        new_node.next = curr.next
        curr.next.prev = new_node
        curr.next = new_node
        new_node.prev = curr
        
    # -----------------------------------
    # Insert After Value
    # -----------------------------------

    def insert_after(self, target, val):
        # Insert a new node immediately after the first occurrence of the target value.
        if not self.head:
            return

        tail = self.head.prev

        if tail.val == target:
            return self.insert_at_end(val)
        
        new_node = Node(val)
        curr = self.head

        while curr.val != target and curr.next != self.head:
            curr = curr.next
        
        if curr == tail and curr.val != target:
            return
        
        new_node.next = curr.next
        curr.next.prev = new_node
        curr.next = new_node
        new_node.prev = curr

    # -----------------------------------
    # Forward Traversal
    # -----------------------------------

    def display_forward(self):
        # Display all nodes once from head to tail in the forward direction.
        if self.head is None:
            return
        
        curr = self.head
        while True:
            print(str(curr.val), end = " <-> ")
            curr = curr.next
            if curr == self.head:
                break
        
        print("HEAD")        

    # -----------------------------------
    # Backward Traversal
    # -----------------------------------

    def display_backward(self):
        # Display all nodes once from tail to head in the backward direction.
        if self.head is None:
            return
        
        tail = self.head.prev
        curr = tail

        while True:
            print(str(tail.val), end = " <-> ")
            tail = tail.prev
            if tail == curr:
                break
            
        print("TAIL")
                

    # -----------------------------------
    # Search
    # -----------------------------------

    def search(self, target):
        # Return True if the target value exists in the list; otherwise return False.
        if self.head is None:
            return False
        
        curr = self.head
        
        while True:
            if curr.val == target:
                return True
            
            curr = curr.next
            
            if curr == self.head:
                break
        
        return False
        
    # -----------------------------------
    # Get Node
    # -----------------------------------

    def get(self, pos):
        # Return the node at the specified position, or None if the position is invalid.
        if self.head is None:
            return
        
        n = len(self)
        if (pos < 0) or (pos > n - 1):
            return
        
        c = 0
        curr = self.head

        while c < pos:
            curr = curr.next
            c += 1
        
        return curr
        

    # -----------------------------------
    # Set Node Value
    # -----------------------------------

    def set(self, pos, new_val):
        # Update the value of the node at the specified position if it exists.
        node = self.get(pos)

        if node:
            node.val = new_val

    # -----------------------------------
    # Delete Beginning
    # -----------------------------------

    def delete_at_beginning(self):
        # Delete the first node while maintaining the circular doubly linked list.
        if self.head is None:
            return
        
        if self.head.next == self.head:
            self.head = None
            return
        
        curr = self.head
        nxt = self.head.next
        tail = self.head.prev

        curr.next = None
        curr.prev = None
        nxt.prev = tail
        tail.next = nxt
        self.head = nxt

    # -----------------------------------
    # Delete End
    # -----------------------------------

    def delete_at_end(self):
        # Delete the last node while maintaining the circular doubly linked list.
        if self.head is None:
            return 
        
        if self.head.next == self.head:
            self.head = None
            return 
        
        tail = self.head.prev
        new_tail = tail.prev

        tail.prev = None
        tail.next = None
        new_tail.next = self.head
        self.head.prev = new_tail


    # -----------------------------------
    # Delete at Position
    # -----------------------------------

    def delete_at_middle(self, pos):
        # Delete the node at the specified position if the position is valid.
        if self.head is None:
            return
        
        n = len(self)
        if (pos < 0) or (pos > n - 1):
            return
        
        if self.head.next == self.head:
            if pos == 0:
                self.head = None
                return
            else:
                return
        
        if pos == 0:
            return self.delete_at_beginning()
        
        if pos == n - 1:
            return self.delete_at_end()
            
        curr = self.head
        c = 0

        while c < pos:
            curr = curr.next
            c += 1
        
        nxt_node = curr.next
        prev_node = curr.prev

        nxt_node.prev = prev_node
        prev_node.next = nxt_node
        curr.next = None
        curr.prev = None


    # -----------------------------------
    # Delete by Value
    # -----------------------------------

    def delete_by_value(self, val):
    # Delete the first node whose value matches the given value.

        if self.head is None:
            return

        # Single node
        if self.head.next == self.head:
            if self.head.val == val:
                self.head = None
            return

        # Head
        if self.head.val == val:
            return self.delete_at_beginning()

        # Tail
        if self.head.prev.val == val:
            return self.delete_at_end()

        curr = self.head.next

        # Search for the value (excluding head and tail)
        while curr != self.head.prev:
            if curr.val == val:
                break
            curr = curr.next

        # Value not found
        if curr == self.head.prev:
            return

        prev_node = curr.prev
        nxt_node = curr.next

        prev_node.next = nxt_node
        nxt_node.prev = prev_node

        curr.next = None
        curr.prev = None

    # -----------------------------------
    # Reverse CDLL
    # -----------------------------------

    def reverse(self):
        # Reverse the circular doubly linked list by swapping each node's next and prev pointers.
        if self.head is None:
            return
        
        curr = self.head
        prev_node = None
        while True:
            curr.prev, curr.next = curr.next, curr.prev
            prev_node = curr
            curr = curr.prev
        
            if curr == self.head:
                break

        self.head = prev_node

    # -----------------------------------
    # Find Middle Node
    # -----------------------------------

    def find_middle(self):
        # Return the middle node using the slow and fast pointer technique.
        if self.head is None:
            return

        slow = self.head
        fast = self.head

        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next

        return slow

    # -----------------------------------
    # Length
    # -----------------------------------

    def __len__(self):
        # Return the total number of nodes in the circular doubly linked list.
        if self.head is None:
            return 0

        curr = self.head
        c = 0
        while curr.next != self.head:
            c += 1
            curr = curr.next
        return c + 1

    # -----------------------------------
    # String Representation
    # -----------------------------------

    def __str__(self):
        # Return a string representation of the circular doubly linked list.
        s = ""
        curr = self.head

        while True:
            s += (str(curr.val) + " <-> ")

            curr = curr.next

            if curr == self.head:
                break

        s += "HEAD"
        return s