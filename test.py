def delete_at_position(self, pos):
    if self.head is None:
        return

    if pos < 0:
        return

    if pos == 0:
        nxt = self.head.next
        self.head.next = None
        self.head = nxt
        return

    curr = self.head
    c = 0

    while curr and c < pos - 1:
        curr = curr.next
        c += 1

    if curr.next is None:
        return

    nxt = curr.next
    curr.next = nxt.next
    nxt.next = None
