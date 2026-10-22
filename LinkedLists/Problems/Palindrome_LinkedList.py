"""
LOGIC: Palindrome Linked List

1. Use slow and fast pointers to find the midpoint.
2. Set second to slow.next to identify the second half.
3. Disconnect the two halves by setting slow.next = None.
4. Reverse the second half using the iterative reversal technique.
5. Compare the first half with the reversed second half, node by node.
6. If any values differ, return False.
7. If all corresponding values match, return True.

Time Complexity: O(n)
Auxiliary Space Complexity: O(1)

Note: This implementation modifies the linked list by splitting it
and reversing its second half. It does not restore the original list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode | None) -> bool:
    # Step 1: Find the midpoint
    slow, fast = head, head

    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Separate the second half
    second = slow.next
    slow.next = None

    # Step 3: Reverse the second half
    prev = None
    curr = second

    while curr:
        nxt_node = curr.next
        curr.next = prev
        prev = curr
        curr = nxt_node

    # Step 4: Compare both halves
    first, second = head, prev

    while first and second:
        if first.val != second.val:
            return False

        first = first.next
        second = second.next

    return True


# Helper function: Build a linked list from a Python list
def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy

    for value in values:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next


# Helper function: Print a linked list
def print_linked_list(head):
    values = []
    curr = head

    while curr:
        values.append(str(curr.val))
        curr = curr.next

    print(" -> ".join(values) if values else "Empty list")


# Test cases
def main():
    test_cases = [
        ("Even-length palindrome", [1, 2, 2, 1], True),
        ("Odd-length palindrome", [1, 2, 3, 2, 1], True),
        ("Not a palindrome", [1, 2, 3], False),
        ("Single node", [7], True),
        ("Empty list", [], True),
        ("All values identical", [4, 4, 4, 4], True),
        ("Two different nodes", [1, 2], False),
        ("Two identical nodes", [5, 5], True),
        ("Negative values", [-1, 2, -1], True),
        ("Duplicate values, not a palindrome", [1, 2, 2, 3], False),
        ("Longer palindrome", [1, 2, 3, 4, 3, 2, 1], True),
        ("Different first and last values", [1, 2, 3, 1], False),
    ]

    for name, values, expected in test_cases:
        head = build_linked_list(values)

        print(f"\nTest: {name}")
        print("Input:", end=" ")
        print_linked_list(head)

        result = isPalindrome(head)

        print("Expected:", expected)
        print("Actual:  ", result)
        print("Status:  ", "PASS" if result == expected else "FAIL")


if __name__ == "__main__":
    main()
