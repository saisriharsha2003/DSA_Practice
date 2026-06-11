class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self, values=None):
        self.head = None

        if values:
            for val in values:
                self.insert_at_end(val)

    # -----------------------------------
    # Insert at Beginning
    # -----------------------------------

    def insert_at_beginning(self, val):

        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # -----------------------------------
    # Insert at End
    # -----------------------------------

    def insert_at_end(self, val):

        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr

    # -----------------------------------
    # Insert at Position
    # -----------------------------------

    def insert_at_middle(self, pos, val):

        if pos < 0:
            return

        if pos == 0:
            self.insert_at_beginning(val)
            return

        curr = self.head
        count = 0

        while curr and count < pos - 1:
            curr = curr.next
            count += 1

        if curr is None:
            return

        new_node = Node(val)

        new_node.next = curr.next
        new_node.prev = curr

        if curr.next:
            curr.next.prev = new_node

        curr.next = new_node

    # -----------------------------------
    # Insert Before Value
    # -----------------------------------

    def insert_before(self, target, val):

        curr = self.head

        while curr and curr.val != target:
            curr = curr.next

        if curr is None:
            return

        if curr == self.head:
            self.insert_at_beginning(val)
            return

        new_node = Node(val)

        prev_node = curr.prev

        prev_node.next = new_node
        new_node.prev = prev_node

        new_node.next = curr
        curr.prev = new_node

    # -----------------------------------
    # Insert After Value
    # -----------------------------------

    def insert_after(self, target, val):

        curr = self.head

        while curr and curr.val != target:
            curr = curr.next

        if curr is None:
            return

        new_node = Node(val)

        new_node.next = curr.next
        new_node.prev = curr

        if curr.next:
            curr.next.prev = new_node

        curr.next = new_node

    # -----------------------------------
    # Forward Traversal
    # -----------------------------------

    def display_forward(self):

        curr = self.head

        while curr:
            print(curr.val, end=" <-> ")
            curr = curr.next

        print("None")

    # -----------------------------------
    # Backward Traversal
    # -----------------------------------

    def display_backward(self):

        curr = self.head

        if curr is None:
            return

        while curr.next:
            curr = curr.next

        while curr:
            print(curr.val, end=" <-> ")
            curr = curr.prev

        print("None")

    # -----------------------------------
    # Search
    # -----------------------------------

    def search(self, target):

        curr = self.head

        while curr:

            if curr.val == target:
                return True

            curr = curr.next

        return False

    # -----------------------------------
    # Get Node
    # -----------------------------------

    def get(self, pos):

        if pos < 0:
            return None

        curr = self.head
        count = 0

        while curr:

            if count == pos:
                return curr

            curr = curr.next
            count += 1

        return None

    # -----------------------------------
    # Set Node Value
    # -----------------------------------

    def set(self, pos, new_val):

        node = self.get(pos)

        if node:
            node.val = new_val

    # -----------------------------------
    # Delete Beginning
    # -----------------------------------

    def delete_at_beginning(self):

        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        self.head = self.head.next
        self.head.prev = None

    # -----------------------------------
    # Delete End
    # -----------------------------------

    def delete_at_end(self):

        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.prev.next = None

    # -----------------------------------
    # Delete at Position
    # -----------------------------------

    def delete_at_middle(self, pos):

        node = self.get(pos)

        if node is None:
            return

        if node == self.head:
            self.delete_at_beginning()
            return

        if node.next is None:
            self.delete_at_end()
            return

        node.prev.next = node.next
        node.next.prev = node.prev

    # -----------------------------------
    # Delete by Value
    # -----------------------------------

    def delete_by_value(self, val):

        curr = self.head

        while curr and curr.val != val:
            curr = curr.next

        if curr is None:
            return

        if curr == self.head:
            self.delete_at_beginning()
            return

        if curr.next is None:
            self.delete_at_end()
            return

        curr.prev.next = curr.next
        curr.next.prev = curr.prev

    # -----------------------------------
    # Reverse DLL
    # -----------------------------------

    def reverse(self):

        curr = self.head
        prev_node = None

        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            prev_node = curr
            curr = curr.prev

        self.head = prev_node

    # -----------------------------------
    # Find Middle Node
    # -----------------------------------

    def find_middle(self):

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # -----------------------------------
    # Length
    # -----------------------------------

    def __len__(self):

        count = 0
        curr = self.head

        while curr:
            count += 1
            curr = curr.next

        return count

    # -----------------------------------
    # String Representation
    # -----------------------------------

    def __str__(self):

        curr = self.head
        result = ""

        while curr:
            result += str(curr.val) + " <-> "
            curr = curr.next

        result += "None"

        return result

# ----------------------------
# Example Usage
# ----------------------------
if __name__ == "__main__":

    # Create initial DLL: 1 <-> 2 <-> 3 <-> None
    dll = DoublyLinkedList([1, 2, 3])

    print(dll)  # 1 <-> 2 <-> 3 <-> None

    # Forward Traversal
    dll.display_forward()   # 1 <-> 2 <-> 3 <-> None

    # Backward Traversal
    dll.display_backward()  # 3 <-> 2 <-> 1 <-> None

    # ----------------------------
    # Insertions
    # ----------------------------

    dll.insert_at_beginning(0)
    print(dll)  # 0 <-> 1 <-> 2 <-> 3 <-> None

    dll.insert_at_end(4)
    print(dll)  # 0 <-> 1 <-> 2 <-> 3 <-> 4 <-> None

    dll.insert_at_middle(2, 99)
    print(dll)  # 0 <-> 1 <-> 99 <-> 2 <-> 3 <-> 4 <-> None

    dll.insert_before(99, 50)
    print(dll)  # 0 <-> 1 <-> 50 <-> 99 <-> 2 <-> 3 <-> 4 <-> None

    dll.insert_after(99, 100)
    print(dll)  # 0 <-> 1 <-> 50 <-> 99 <-> 100 <-> 2 <-> 3 <-> 4 <-> None

    # ----------------------------
    # Search
    # ----------------------------

    print(dll.search(100))  # True
    print(dll.search(500))  # False

    # ----------------------------
    # Get Method
    # ----------------------------

    print(dll.get(0).val)   # 0
    print(dll.get(3).val)   # 99
    print(dll.get(7).val)   # 4
    print(dll.get(20))      # None

    # ----------------------------
    # Set Method
    # ----------------------------

    dll.set(3, 999)
    dll.set(0, -1)

    print(dll)
    # -1 <-> 1 <-> 50 <-> 999 <-> 100 <-> 2 <-> 3 <-> 4 <-> None

    # ----------------------------
    # Length
    # ----------------------------

    print(len(dll))  # 8

    # ----------------------------
    # Deletions
    # ----------------------------

    dll.delete_at_beginning()
    print(dll)
    # 1 <-> 50 <-> 999 <-> 100 <-> 2 <-> 3 <-> 4 <-> None

    dll.delete_at_end()
    print(dll)
    # 1 <-> 50 <-> 999 <-> 100 <-> 2 <-> 3 <-> None

    dll.delete_at_middle(2)
    print(dll)
    # 1 <-> 50 <-> 100 <-> 2 <-> 3 <-> None

    dll.delete_by_value(100)
    print(dll)
    # 1 <-> 50 <-> 2 <-> 3 <-> None

    # ----------------------------
    # Reverse DLL
    # ----------------------------

    dll.reverse()
    print(dll)
    # 3 <-> 2 <-> 50 <-> 1 <-> None

    dll.display_backward()
    # 1 <-> 50 <-> 2 <-> 3 <-> None

    # ----------------------------
    # Find Middle Node
    # ----------------------------

    middle = dll.find_middle()

    if middle:
        print(middle.val)  # 50