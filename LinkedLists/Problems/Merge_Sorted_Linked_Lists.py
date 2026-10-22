"""
LOGIC: Merge Two Sorted Lists

1. Create a dummy node to simplify building the merged list.
2. Compare the current nodes of both sorted lists.
3. Attach the smaller node to the merged list and move its pointer.
4. When one list ends, attach the remaining part of the other list.
5. Return dummy.next as the merged list's head.

Time Complexity: O(m + n)
Space Complexity: O(1) auxiliary space
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


def mergeTwoLists(list1, list2):
    dummy = ListNode(0)
    curr = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next

        curr = curr.next

    curr.next = list1 if list1 else list2

    return dummy.next


def main():
    # Example 1: Normal case
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])
    print("Example 1: Normal case")
    print_linked_list(mergeTwoLists(list1, list2))
    # Expected: [1, 1, 2, 3, 4, 4]

    # Example 2: Both lists empty
    list1 = build_linked_list([])
    list2 = build_linked_list([])
    print("Example 2: Both lists empty")
    print_linked_list(mergeTwoLists(list1, list2))
    # Expected: []

    # Example 3: First list empty
    list1 = build_linked_list([])
    list2 = build_linked_list([0])
    print("Example 3: First list empty")
    print_linked_list(mergeTwoLists(list1, list2))
    # Expected: [0]

    # Example 4: Second list empty
    list1 = build_linked_list([1, 2, 3])
    list2 = build_linked_list([])
    print("Example 4: Second list empty")
    print_linked_list(mergeTwoLists(list1, list2))
    # Expected: [1, 2, 3]

    # Example 5: Different lengths
    list1 = build_linked_list([1, 5, 8])
    list2 = build_linked_list([2, 3])
    print("Example 5: Different lengths")
    print_linked_list(mergeTwoLists(list1, list2))
    # Expected: [1, 2, 3, 5, 8]

    # Example 6: All values equal
    list1 = build_linked_list([2, 2, 2])
    list2 = build_linked_list([2, 2])
    print("Example 6: Duplicate values")
    print_linked_list(mergeTwoLists(list1, list2))
    # Expected: [2, 2, 2, 2, 2]

    # Example 7: Negative values
    list1 = build_linked_list([-5, -1, 3])
    list2 = build_linked_list([-4, 0, 7])
    print("Example 7: Negative and positive values")
    print_linked_list(mergeTwoLists(list1, list2))
    # Expected: [-5, -4, -1, 0, 3, 7]

    # Example 8: One list contains smaller values throughout
    list1 = build_linked_list([1, 2, 3])
    list2 = build_linked_list([10, 11])
    print("Example 8: All first-list values are smaller")
    print_linked_list(mergeTwoLists(list1, list2))
    # Expected: [1, 2, 3, 10, 11]


if __name__ == "__main__":
    main()
