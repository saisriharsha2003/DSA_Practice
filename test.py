def find_middle(self):

    slow = self.head
    fast = self.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
