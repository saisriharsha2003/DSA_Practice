# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ----------------------------
# Linked List Operations
# ----------------------------

# 1. Traversal
def traverse(head: ListNode) -> list:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

# 2. Insertion

# 2.1 Insert at Beginning
def insert_at_beginning(head: ListNode, val: int) -> ListNode:
    return ListNode(val, head)

# 2.2 Insert at End
def insert_at_end(head: ListNode, val: int) -> ListNode:
    new_node = ListNode(val)
    if not head:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head

# 2.3 Insert at Position (0-indexed)
def insert_at_position(head: ListNode, pos: int, val: int) -> ListNode:
    if pos == 0:
        return ListNode(val, head)
    curr = head
    idx = 0
    while curr and idx < pos - 1:
        curr = curr.next
        idx += 1
    if not curr:
        return head
    new_node = ListNode(val, curr.next)
    curr.next = new_node
    return head

# 3. Deletion

# 3.1 Delete at Position (0-indexed)
def delete_at_position(head: ListNode, pos: int) -> ListNode:
    if not head:
        return None
    if pos == 0:
        return head.next
    curr = head
    idx = 0
    while curr.next and idx < pos - 1:
        curr = curr.next
        idx += 1
    if curr.next:
        curr.next = curr.next.next
    return head

# 3.2 Delete by Value
def delete_by_value(head: ListNode, val: int) -> ListNode:
    dummy = ListNode(0, head)
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
            break
        curr = curr.next
    return dummy.next

# 4. Searching
def search(head: ListNode, val: int) -> int:
    idx = 0
    curr = head
    while curr:
        if curr.val == val:
            return idx
        curr = curr.next
        idx += 1
    return -1

# 5. Updating / Modification

# 5.1 Update at Position
def update_at_position(head: ListNode, pos: int, new_val: int) -> ListNode:
    idx = 0
    curr = head
    while curr and idx < pos:
        curr = curr.next
        idx += 1
    if curr:
        curr.val = new_val
    return head

# 5.2 Update First Matching Value
def update_first_by_value(head: ListNode, old_val: int, new_val: int) -> ListNode:
    curr = head
    while curr:
        if curr.val == old_val:
            curr.val = new_val
            break
        curr = curr.next
    return head

# 6. Reversal
def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# ----------------------------
# Example Usage
# ----------------------------
if __name__ == "__main__":
    # Create initial list: 1->2->3
    head = ListNode(1, ListNode(2, ListNode(3)))

    print("Original list:", traverse(head))

    # Insertions
    head = insert_at_beginning(head, 0)  # 0->1->2->3
    head = insert_at_end(head, 4)        # 0->1->2->3->4
    head = insert_at_position(head, 2, 99)  # 0->1->99->2->3->4
    print("After insertions:", traverse(head))

    # Deletions
    head = delete_at_position(head, 2)   # remove 99
    head = delete_by_value(head, 0)      # remove 0
    head = remove_nth_from_end(head, 1)  # remove last node (4)
    print("After deletions:", traverse(head))

    # Searching
    print("Index of 2:", search(head, 2))
    print("Index of 100:", search(head, 100))

    # Updating
    head = update_at_position(head, 1, 42)
    head = update_first_by_value(head, 42, 7)
    print("After updates:", traverse(head))

    # Reversal
    head = reverse_list(head)
    print("After reversal:", traverse(head))
