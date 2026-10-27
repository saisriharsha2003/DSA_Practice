
"""
LOGIC: Remove All Duplicate Values from Sorted Linked List

1. Create a dummy node before the head and use a tail pointer
   to track the last retained node.
2. If the current value is repeated, skip its entire group.
3. Otherwise, connect the unique node to the retained list
   and advance the tail.
4. Terminate the retained list to disconnect skipped nodes.
5. Return dummy.next.

Time Complexity: O(n)
Auxiliary Space Complexity: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode | None) -> ListNode | None:
    dummy = ListNode(-1)
    dummy.next = head
    tail = dummy
    curr = head

    while curr:
        # Check whether the current value is duplicated
        if curr.next and curr.val == curr.next.val:
            # Skip every node with this duplicated value
            duplicate_value = curr.val

            while curr and curr.val == duplicate_value:
                curr = curr.next
        else:
            # Keep this unique node
            tail.next = curr
            tail = curr
            curr = curr.next

    # Disconnect any skipped nodes from the retained list
    tail.next = None

    return dummy.next


def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy

    for value in values:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next


def print_linked_list(head):
    if head is None:
        print("Empty list")
        return

    curr = head

    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next

    print("None")


def main():
    # 1. Duplicates at the beginning
    head = build_linked_list([1, 1, 2])
    print("Example 1:")
    print_linked_list(deleteDuplicates(head))  # 2 -> None

    # 2. Duplicates at the beginning, middle, and end
    head = build_linked_list([1, 2, 3, 3, 4, 4, 5])
    print("\nExample 2:")
    print_linked_list(deleteDuplicates(head))  # 1 -> 2 -> 5 -> None

    # 3. All values are duplicated
    head = build_linked_list([5, 5, 5, 5])
    print("\nExample 3:")
    print_linked_list(deleteDuplicates(head))  # Empty list

    # 4. No duplicates
    head = build_linked_list([1, 2, 3, 4])
    print("\nExample 4:")
    print_linked_list(deleteDuplicates(head))  # 1 -> 2 -> 3 -> 4 -> None

    # 5. Empty list
    head = build_linked_list([])
    print("\nExample 5:")
    print_linked_list(deleteDuplicates(head))  # Empty list

    # 6. Single node
    head = build_linked_list([7])
    print("\nExample 6:")
    print_linked_list(deleteDuplicates(head))  # 7 -> None

    # 7. Negative values and multiple duplicate groups
    head = build_linked_list([-3, -3, -1, 0, 0, 2])
    print("\nExample 7:")
    print_linked_list(deleteDuplicates(head))  # -1 -> 2 -> None

    # 8. Duplicates at the end
    head = build_linked_list([1, 2, 2])
    print("\nExample 8:")
    print_linked_list(deleteDuplicates(head))  # 1 -> None

    # 9. Every value appears twice
    head = build_linked_list([1, 1, 2, 2])
    print("\nExample 9:")
    print_linked_list(deleteDuplicates(head))  # Empty list


if __name__ == "__main__":
    main()
