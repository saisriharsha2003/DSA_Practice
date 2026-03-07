"""
This single program demonstrates:
1. Creating a Node Class
2. Creating a Linked List Class
3. Inserting a New Node at the Beginning
4. Inserting a New Node at the End
5. Inserting a New Node in the Middle
6. Traversing Through the Linked List
7. Search Method in Linked List
8. Get Method in Linked List
9. Set Method in Linked List
10. Delete a Node at the Beginning
11. Delete a Node at the End
12. Delete a Node in the Middle
13. Reversing of LinkedList
14. Find Middle node of LinkedList (Slow / Fast Pointer Approach)
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
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        self.length = 0
        
        if values:
            for val in values:
                self.insert_at_end(val)

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

        if pos == 0:
            self.insert_at_begining(val)
            return
        
        if pos == self.length :
            self.insert_at_end(val)
            return

        new_node = Node(val)

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

    # Using __len__ method
    def __len__(self):
        return self.length

    # ------------------------------------------------
    # 7. Search Method in Linked List
    # ------------------------------------------------

    def search(self, target):
        if self.head is None:
            return False
        
        curr = self.head
        while curr:
            if curr.val == target:
                return True         
            curr = curr.next
        
        return False

    # ------------------------------------------------
    # 8. Get Method in Linked List
    # ------------------------------------------------

    def get(self, pos):
        if pos < 0 or pos >= self.length:
            return

        if pos == 0:
            return self.head

        if pos == self.length - 1:
            return self.tail
            
        curr = self.head
        c = 0
        
        while c < pos:
            curr = curr.next
            c += 1
        
        return curr

    # ------------------------------------------------
    # 9. Set Method in Linked List
    # ------------------------------------------------

    def set(self, pos, new_val):
        val_pos = self.get(pos)
        
        if val_pos:
            val_pos.val = new_val
        
    # ------------------------------------------------
    # 10. Delete a node at beginning
    # ------------------------------------------------
    
    def delete_at_beginning(self):
        if self.head is None:
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        self.length -= 1
    
    # ------------------------------------------------
    # 11. Delete a node at the end
    # ------------------------------------------------

    def delete_at_end(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None 
            self.length -= 1
            return

        curr = self.head

        while curr.next != self.tail:
            curr = curr.next
        
        curr.next = None
        self.tail = curr
        self.length -= 1

    # ------------------------------------------------
    # 12. Delete a node at middle
    # ------------------------------------------------

    def delete_at_middle(self, pos):
        if self.head is None:
            return

        if pos < 0 or pos >= self.length:
            return

        if pos == 0:
            self.delete_at_beginning()
            return
        
        if pos == self.length - 1:
            self.delete_at_end()
            return
        
        curr = self.head
        c = 0

        while c < pos - 1:
            curr = curr.next
            c += 1
        
        curr.next = curr.next.next

        self.length -= 1
    
    # ------------------------------------------------
    # 13. Reversing of LinkedList
    # ------------------------------------------------

    def reverse(self):
        prev = None 
        curr = self.head
        self.tail = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    # ------------------------------------------------------------------
    # 14. Find Middle node of LinkedList (Slow / Fast Pointer Approach)
    # ------------------------------------------------------------------

    def find_middle(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow

class Solution(object):
    # ------------------------------------------------
    # 15. Merge two sorted LinkedLists
    # ------------------------------------------------

    def mergeTwoLists(self, l1, l2):

        if l1 is None:
            return l2
            
        if l2 is None:
            return l1
            
        dummy = Node(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1 
                l1 = l1.next 
            else:
                tail.next = l2
                l2 = l2.next
                
            tail = tail.next
            
        if l1:
            tail.next = l1
        else:
            tail.next = l2
            
        return dummy.next
                
    
    # Need to __iter__ and reverse and find_middle (slow / fast) methods

# ----------------------------
# Example Usage
# ----------------------------
if __name__ == "__main__":

    # Create initial list: 1 -> 2 -> 3 -> None
    ll = LinkedList([1,2,3])

    print(ll) # 1 -> 2 -> 3 -> None

    ll.display() # 1 -> 2 -> 3 -> None


    # Insertions
    ll.insert_at_begining(0)  
    ll.display() # 0 -> 1 -> 2 -> 3 -> None
    ll.insert_at_end(4)        
    ll.display() # 0 -> 1-> 2 -> 3 -> 4 -> None
    ll.insert_at_middle(2, 99)  
    ll.display() # 0 -> 1 -> 99 -> 2 -> 3 -> 4 -> None

    # Search 
    print(ll.search(3)) # True
    print(ll.search(100)) # False

    # Get Method
    print(ll.get(0).val) # 0
    print(ll.get(5).val) # 4
    print(ll.get(3).val) # 2
    print(ll.get(25)) # None

    # Set Method
    ll.set(2, 44)
    ll.set(0, 1)
    ll.set(5, 45)
    ll.set(10, 40)
    print(ll)

    # Deletion
    ll.delete_at_beginning()
    ll.display() # 1 -> 99 -> 2 -> 3 -> 45 -> None
    ll.delete_at_end()
    ll.display() # 1 -> 99 -> 2 -> 3 -> None
    ll.delete_at_middle(2)
    ll.display() # 1 -> 44 -> 3 -> None

    # Reversing of LinkedList
    ll.reverse()
    print(ll) # 3 -> 44 -> 1 -> None

    # Find middle node of LinkedList
    print(ll.find_middle().val)

    # Merge two sorted linedlists
    ll1 = LinkedList([1, 2, 4])
    ll2 = LinkedList([1, 3, 4])

    sol = Solution()
    merged_head = sol.mergeTwoLists(ll1.head, ll2.head)

    curr = merged_head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None") # 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None

