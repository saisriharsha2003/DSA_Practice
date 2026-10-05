class Queue:
    """
    A simple Queue implementation using a list.

    Queue follows the FIFO (First In, First Out) principle:
    the first element added is the first one removed.
    """

    def __init__(self):
        """Initialize an empty queue."""
        self.queue = []
        self.length = 0

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.queue.append(item)
        self.length += 1

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.isEmpty():
            return "There are no elements in the Queue"
        
        self.length -= 1
        return self.queue.pop(0)

    def peek(self):
        """Return the front item without removing it."""
        if self.isEmpty():
            return "There are no elements in the Queue"

        return self.queue[0]
    
    def isEmpty(self):
        """Returns whether the queue is empty or not."""
        return self.length == 0
    
    def delete(self):
        """Delete all contents of the queue"""
        self.queue = []
        self.length = 0


def main():
    """Demonstrate and test basic Queue operations."""

    # Create a new queue
    queue = Queue()

    # Test enqueue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    # Test peek()
    print("Front element:", queue.peek())

    # Test dequeue()
    print("Dequeued element:", queue.dequeue())

    # Test peek() after dequeue
    print("Front element:", queue.peek())

    # Test remaining dequeue operations
    print("Dequeued element:", queue.dequeue())
    print("Dequeued element:", queue.dequeue())

    # Test empty queue
    print("Dequeued element:", queue.dequeue())
    print("Front element:", queue.peek())


if __name__ == "__main__":
    main()