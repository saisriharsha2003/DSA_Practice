
"""
LOGIC: Reorder List

1. Find the middle using slow and fast pointers.
2. Split the linked list into two halves.
3. Reverse the second half.
4. Merge both halves alternately.
5. Rearrange existing nodes without changing their values.

Time Complexity: O(n)
Auxiliary Space Complexity: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: ListNode | None) -> None:
    if not head or not head.next:
        return

    slow, fast = head, head

    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None

    curr = second
    prev = None

    while curr:
        nxt_node = curr.next
        curr.next = prev
        prev = curr
        curr = nxt_node

    curr1, curr2 = head, prev

    while curr1 and curr2:
        nxt_node1 = curr1.next
        nxt_node2 = curr2.next

        curr1.next = curr2
        curr2.next = nxt_node1

        curr1 = nxt_node1
        curr2 = nxt_node2


# Build a linked list
def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy

    for value in values:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next


# Print a linked list
def print_linked_list(head):
    curr = head

    if curr is None:
        print("Empty list")
        return

    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next

    print("None")


def main():
    # Example 1: Even-length list
    head = build_linked_list([1, 2, 3, 4])
    print("Before:")
    print_linked_list(head)

    reorderList(head)
    print("After:")
    print_linked_list(head)

    # Example 2: Odd-length list
    head = build_linked_list([1, 2, 3, 4, 5])
    print("\nBefore:")
    print_linked_list(head)

    reorderList(head)
    print("After:")
    print_linked_list(head)

    # Example 3: Empty list
    head = build_linked_list([])
    print("\nEmpty list:")
    reorderList(head)
    print_linked_list(head)

    # Example 4: Single node
    head = build_linked_list([7])
    print("\nSingle node:")
    reorderList(head)
    print_linked_list(head)

    # Example 5: Two nodes
    head = build_linked_list([8, 9])
    print("\nTwo nodes:")
    reorderList(head)
    print_linked_list(head)


if __name__ == "__main__":
    main()
