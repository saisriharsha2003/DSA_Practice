class CircularQueue:
    """
    A Queue implementation using a fixed-size circular array.

    Queue follows the FIFO (First In, First Out) principle.
    """

    def __init__(self, size):
        """Initialize a circular queue with a fixed capacity."""
        self.queue = [None] * size
        self.capacity = size
        self.front = 0
        self.rear = 0
        self.length = 0

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        if self.is_full():
            print("Queue Overflow")
            return
        
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.length += 1

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            print("Queue Underflow")
            return
        
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.length -= 1
        
        return item

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            print("Queue Underflow")
            return
        
        return self.queue[self.front]

    def is_empty(self):
        """Return True if the queue is empty."""
        return self.length == 0

    def is_full(self):
        """Return True if the queue has reached its capacity."""
        return self.length == self.capacity

    def size(self):
        """Return the number of elements currently in the queue."""
        return self.length

    def delete(self):
        """Delete all elements from the queue."""
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = 0
        self.length = 0
    
    def __str__(self):
        """Return the queue contents as a string."""
        return str(self.queue)


def main():
    """Demonstrate and test basic Circular Queue operations."""

    # Create a circular queue with capacity 3
    queue = CircularQueue(3)

    # Test enqueue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Queue:", queue)

    # Test overflow
    queue.enqueue(40)

    # Test peek()
    print("Front element:", queue.peek())

    # Test dequeue()
    print("Dequeued element:", queue.dequeue())
    print("Dequeued element:", queue.dequeue())

    # Add elements again to demonstrate circular behavior
    queue.enqueue(40)
    queue.enqueue(50)

    print("Queue:", queue)

    # Remove remaining elements
    print("Dequeued element:", queue.dequeue())
    print("Dequeued element:", queue.dequeue())
    print("Dequeued element:", queue.dequeue())

    # Test underflow
    queue.dequeue()


if __name__ == "__main__":
    main()