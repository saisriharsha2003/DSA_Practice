"""
LOGIC: Intersection of Two Linked Lists (Two Pointers)

1. Initialize p1 at headA and p2 at headB.
2. Move both pointers one node at a time.
3. When p1 reaches None, redirect it to headB.
4. When p2 reaches None, redirect it to headA.
5. If the lists intersect, both pointers meet at the same shared node.
6. If they do not intersect, both eventually become None.
7. Return p1, which is either the shared node or None.

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA, headB):
    p1, p2 = headA, headB

    while p1 is not p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA

    return p1


def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


def main():
    # Example 1: Normal intersection after different prefixes
    # A: 1 -> 2 -> 8 -> 10 -> None
    # B: 3 -> 8 -> 10 -> None
    shared = ListNode(8, ListNode(10))
    headA = ListNode(1, ListNode(2, shared))
    headB = ListNode(3, shared)

    print("Example 1: Normal intersection")
    print("List A:", end=" ")
    printList(headA)
    print("List B:", end=" ")
    printList(headB)

    result = getIntersectionNode(headA, headB)
    print("Intersection:", result.val if result else None)
    print()

    # Example 2: No intersection (same values, different nodes)
    headA = ListNode(1, ListNode(2, ListNode(3)))
    headB = ListNode(1, ListNode(2, ListNode(3)))

    print("Example 2: No intersection")
    print("List A:", end=" ")
    printList(headA)
    print("List B:", end=" ")
    printList(headB)

    result = getIntersectionNode(headA, headB)
    print("Intersection:", result.val if result else None)
    print()

    # Example 3: Both heads are the same node
    shared = ListNode(5, ListNode(6))
    headA = shared
    headB = shared

    print("Example 3: Identical heads")
    print("List A:", end=" ")
    printList(headA)
    print("List B:", end=" ")
    printList(headB)

    result = getIntersectionNode(headA, headB)
    print("Intersection:", result.val if result else None)
    print()

    # Example 4: Intersection at the head of List A
    headA = ListNode(7, ListNode(8))
    headB = ListNode(4, ListNode(5, headA))

    print("Example 4: Intersection at head of A")
    print("List A:", end=" ")
    printList(headA)
    print("List B:", end=" ")
    printList(headB)

    result = getIntersectionNode(headA, headB)
    print("Intersection:", result.val if result else None)
    print()

    # Example 5: One list is empty
    headA = None
    headB = ListNode(1, ListNode(2))

    print("Example 5: One list empty")
    print("List A:", end=" ")
    printList(headA)
    print("List B:", end=" ")
    printList(headB)

    result = getIntersectionNode(headA, headB)
    print("Intersection:", result.val if result else None)
    print()

    # Example 6: Both lists are empty
    headA = None
    headB = None

    print("Example 6: Both lists empty")
    print("List A:", end=" ")
    printList(headA)
    print("List B:", end=" ")
    printList(headB)

    result = getIntersectionNode(headA, headB)
    print("Intersection:", result.val if result else None)
    print()

    # Example 7: Intersection at the last node
    shared = ListNode(99)
    headA = ListNode(1, ListNode(2, shared))
    headB = ListNode(3, shared)

    print("Example 7: Intersection at last node")
    print("List A:", end=" ")
    printList(headA)
    print("List B:", end=" ")
    printList(headB)

    result = getIntersectionNode(headA, headB)
    print("Intersection:", result.val if result else None)
    print()

    # Example 8: Single-node lists with different nodes
    headA = ListNode(42)
    headB = ListNode(42)

    print("Example 8: Separate single-node lists")
    print("List A:", end=" ")
    printList(headA)
    print("List B:", end=" ")
    printList(headB)

    result = getIntersectionNode(headA, headB)
    print("Intersection:", result.val if result else None)


if __name__ == "__main__":
    main()
