class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.length = 0
        self.k = k
        
    def insertFront(self, value: int) -> bool:
        new_node = ListNode(value)

        if self.head is None:
            self.tail = self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.length += 1
            return True
        
        if self.length < self.k:
            self.head.prev = new_node
            new_node.next = self.head

            self.head = new_node
            new_node.prev = self.tail

            self.tail.next = new_node
            self.length += 1
            return True
            
        return False
            
    def insertLast(self, value: int) -> bool:
        new_node = ListNode(value)

        if self.head is None:
            self.head = self.tail = new_node
            new_node.prev = new_node
            new_node.next = new_node
            self.length += 1
            return True
        
        if self.length < self.k:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = self.head

            self.tail = new_node
            self.head.prev = new_node

            self.length += 1
            return True
        
        return False

    def deleteFront(self) -> bool:
        if self.head is None:
            return False
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
            return True

        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head
        self.length -= 1
        return True
        
    def deleteLast(self) -> bool:
        if self.head is None:
            return False
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
            return True
        
        prev_node = self.tail.prev
        self.tail = prev_node
        prev_node.next = self.head
        self.head.prev = prev_node
        self.length -= 1
        return True
        
    def getFront(self) -> int:
        return self.head.val if self.head else -1

    def getRear(self) -> int:
        return self.tail.val if self.tail else -1
        

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()