def oddEvenList(head: ListNode | None) -> ListNode | None:
    curr = head
    even = ListNode(-1)
    odd = ListNode(-1)
    tail = dummy
    e, o = even, odd
    while curr:
        nxt_node = curr.next
        if curr.val % 2 == 0:
            e.next = curr
            e = e.next
        else:
            o.next = curr
            o = o.next
        
        curr.next = None
        curr = nxt_node
    
    o = odd
    while o.next:
        o = o.next
    
    o.next = even.next
    return odd.next