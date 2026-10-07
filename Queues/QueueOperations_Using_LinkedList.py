class Node:
    """Represents a node in the linked list."""

    def __init__(self, val):
        """Initialize a node with a value."""
        self.val = val
        self.next = None


class Queue:
    """
    A Queue implementation using a singly linked list.

    Queue follows the FIFO (First In, First Out) principle.
    """

    def __init__(self):
        """Initialize an empty queue."""
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        new_node = Node(item)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            self.length += 1
            return
        
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            return "Queue Underflow"
        
        item = self.front
        if self.length == 1:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.length -= 1
        return item.val

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            return "Queue Underflow"

        return self.front.val

    def is_empty(self):
        """Return True if the queue is empty."""
        return self.length == 0

    def size(self):
        """Return the number of elements currently in the queue."""
        return self.length

    def delete(self):
        """Delete all elements from the queue."""
        self.front = None
        self.rear = None 
        self.length = 0

    def __str__(self):
        """Return string representation of the queue."""
        if self.is_empty():
            return "None"

        curr = self.front
        res = ""

        while curr.next:
            res += str(curr.val) + " -> "
            curr = curr.next

        res += str(curr.val) + " -> None"
        return res

def main():
    """Demonstrate and test basic Queue operations."""

    # Create a new queue
    queue = Queue()

    # Test enqueue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    
    print(queue)

    # Test peek()
    print("Front element:", queue.peek())

    # Test dequeue()
    print("Dequeued element:", queue.dequeue())
    print(queue)

    # Test peek() after dequeue
    print("Front element:", queue.peek())

    # Test remaining dequeue operations
    print("Dequeued element:", queue.dequeue())
    print("Dequeued element:", queue.dequeue())
    print(queue)

    # Test empty queue
    print("Dequeued element:", queue.dequeue())
    print("Front element:", queue.peek())


if __name__ == "__main__":
    main()