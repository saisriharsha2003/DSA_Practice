def swapPairs(head: ListNode | None) -> ListNode | None:
    if not head:
        return None
    
    dummy = ListNode(-1)
    tail = dummy
    tail.next = head
    curr = head

    while curr and curr.next:
        first = curr
        second = curr.next

        first.next = second.next
        tail.next = second
        second.next = first
        tail = first
        curr = second.next
    
    return dummy.next