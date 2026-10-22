"""
LOGIC: Detect Cycle in a Linked List (Floyd's Algorithm)

1. Initialize slow and fast pointers at the head.
2. Move slow by one node and fast by two nodes.
3. If both pointers meet, a cycle exists.
4. If fast or fast.next becomes None, no cycle exists.

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
    # Use this only for lists known to be acyclic.
    values = []
    curr = head

    while curr:
        values.append(curr.val)
        curr = curr.next

    print(values)


def hasCycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


def main():
    # Example 1: Normal list without a cycle
    head = build_linked_list([1, 2, 3, 4])
    print("Example 1: No cycle")
    print_linked_list(head)
    print("Has cycle:", hasCycle(head))
    # Expected: False

    # Example 2: Empty list
    head = None
    print("\nExample 2: Empty list")
    print("Has cycle:", hasCycle(head))
    # Expected: False

    # Example 3: Single node without a cycle
    head = ListNode(1)
    print("\nExample 3: Single node without a cycle")
    print("Has cycle:", hasCycle(head))
    # Expected: False

    # Example 4: Single node pointing to itself
    head = ListNode(1)
    head.next = head
    print("\nExample 4: Single node cycle")
    print("Has cycle:", hasCycle(head))
    # Expected: True

    # Example 5: Cycle starts at the head
    head = build_linked_list([1, 2, 3])
    tail = head

    while tail.next:
        tail = tail.next

    tail.next = head
    print("\nExample 5: Cycle starts at the head")
    print("Has cycle:", hasCycle(head))
    # Expected: True

    # Example 6: Cycle starts in the middle
    head = build_linked_list([1, 2, 3, 4, 5])
    node3 = head.next.next
    tail = head

    while tail.next:
        tail = tail.next

    tail.next = node3
    print("\nExample 6: Cycle starts in the middle")
    print("Has cycle:", hasCycle(head))
    # Expected: True

    # Example 7: Two-node cycle
    first = ListNode(1)
    second = ListNode(2)
    first.next = second
    second.next = first

    print("\nExample 7: Two-node cycle")
    print("Has cycle:", hasCycle(first))
    # Expected: True


if __name__ == "__main__":
    main()
