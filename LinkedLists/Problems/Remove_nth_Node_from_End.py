"""
LOGIC: Remove Nth Node From End

1. Create a dummy node before the head.
2. Move the first pointer n + 1 steps ahead of the dummy.
3. Move both pointers one step at a time until first reaches None.
4. The second pointer now points to the node before the target.
5. Skip the target node by updating second.next.
6. Return dummy.next because the original head may have been removed.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values):
    dummy = ListNode()
    curr = dummy

    for value in values:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next


def print_linked_list(head):
    values = []
    curr = head

    while curr:
        values.append(curr.val)
        curr = curr.next

    print(values)


def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    first = dummy
    second = dummy

    # Move first n+1 steps ahead.
    for _ in range(n + 1):
        if first is None:
            return head  # Invalid n; leave list unchanged
        first = first.next

    # Move both pointers until first reaches None.
    while first:
        first = first.next
        second = second.next

    # Remove the target node.
    second.next = second.next.next

    return dummy.next


def main():
    # Example 1: Remove a middle node
    head = build_linked_list([1, 2, 3, 4, 5])
    print("Example 1: Remove 2nd node from the end")
    print("Before:", end=" ")
    print_linked_list(head)
    head = removeNthFromEnd(head, 2)
    print("After: ", end=" ")
    print_linked_list(head)
    # Expected: [1, 2, 3, 5]

    # Example 2: Remove the last node
    head = build_linked_list([1, 2, 3])
    print("\nExample 2: Remove last node")
    head = removeNthFromEnd(head, 1)
    print_linked_list(head)
    # Expected: [1, 2]

    # Example 3: Remove the head
    head = build_linked_list([1, 2, 3])
    print("\nExample 3: Remove head")
    head = removeNthFromEnd(head, 3)
    print_linked_list(head)
    # Expected: [2, 3]

    # Example 4: Single-node list
    head = build_linked_list([1])
    print("\nExample 4: Single-node list")
    head = removeNthFromEnd(head, 1)
    print_linked_list(head)
    # Expected: []

    # Example 5: Two-node list, remove head
    head = build_linked_list([1, 2])
    print("\nExample 5: Two nodes, remove head")
    head = removeNthFromEnd(head, 2)
    print_linked_list(head)
    # Expected: [2]

    # Example 6: Two-node list, remove tail
    head = build_linked_list([1, 2])
    print("\nExample 6: Two nodes, remove tail")
    head = removeNthFromEnd(head, 1)
    print_linked_list(head)
    # Expected: [1]

    # Example 7: Empty list
    head = None
    print("\nExample 7: Empty list")
    head = removeNthFromEnd(head, 1)
    print_linked_list(head)
    # Expected: []

    # Example 8: Invalid n (outside the usual problem constraints)
    head = build_linked_list([1, 2, 3])
    print("\nExample 8: Invalid n = 4")
    head = removeNthFromEnd(head, 4)
    print_linked_list(head)
    # Expected with this implementation: [1, 2, 3]


if __name__ == "__main__":
    main()
