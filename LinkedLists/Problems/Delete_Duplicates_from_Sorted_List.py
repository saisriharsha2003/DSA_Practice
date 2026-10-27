
"""
LOGIC: Remove Duplicates from Sorted Linked List

1. Start at the head and compare each node with its next node.
2. If both values are equal, skip the next node.
3. Otherwise, move to the next node.
4. Repeat until there is no next node.
5. Return the original head.

Time Complexity: O(n)
Auxiliary Space Complexity: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode | None) -> ListNode | None:
    curr = head

    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head


def build_linked_list(values):
    dummy = ListNode()
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


def main():
    # 1. Duplicates at the beginning
    head = build_linked_list([1, 1, 2])
    print("Example 1:")
    print_linked_list(deleteDuplicates(head))

    # 2. Duplicates at the beginning, middle, and end
    head = build_linked_list([1, 1, 2, 3, 3])
    print("\nExample 2:")
    print_linked_list(deleteDuplicates(head))

    # 3. All values are duplicates
    head = build_linked_list([5, 5, 5, 5])
    print("\nExample 3:")
    print_linked_list(deleteDuplicates(head))

    # 4. No duplicates
    head = build_linked_list([1, 2, 3, 4])
    print("\nExample 4:")
    print_linked_list(deleteDuplicates(head))

    # 5. Empty linked list
    head = build_linked_list([])
    print("\nExample 5 (empty list):")
    print_linked_list(deleteDuplicates(head))

    # 6. Single node
    head = build_linked_list([7])
    print("\nExample 6 (single node):")
    print_linked_list(deleteDuplicates(head))

    # 7. Negative values and multiple duplicate groups
    head = build_linked_list([-3, -3, -1, 0, 0, 2])
    print("\nExample 7:")
    print_linked_list(deleteDuplicates(head))

    # 8. Two identical nodes
    head = build_linked_list([9, 9])
    print("\nExample 8:")
    print_linked_list(deleteDuplicates(head))


if __name__ == "__main__":
    main()
