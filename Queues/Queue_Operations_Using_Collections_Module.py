from collections import deque


class Queue:
    """
    A Queue implementation using collections.deque.

    Queue follows the FIFO (First In, First Out) principle.
    """

    def __init__(self):
        """Initialize an empty queue."""
        self.queue = deque()

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            return "Queue Underflow"

        return self.queue.popleft()

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            return "Queue Underflow"

        return self.queue[0]

    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of elements in the queue."""
        return self.queue

    def delete(self):
        """Delete all elements from the queue."""
        self.queue.clear()

    def __str__(self):
        """Return string representation of the queue."""
        return str(self.queue)


def main():
    """Demonstrate and test the Queue."""

    queue = Queue()

    # Test enqueue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    # Test __str__()
    print("Queue:", queue)

    # Test peek()
    print("Front element:", queue.peek())

    # Test dequeue()
    print("Dequeued element:", queue.dequeue())

    # Test size()
    print("Queue size:", queue.size())

    # Test is_empty()
    print("Is queue empty?", queue.is_empty())

    # Test remaining elements
    print("Dequeued element:", queue.dequeue())
    print("Dequeued element:", queue.dequeue())

    # Test empty queue
    print("Dequeued element:", queue.dequeue())
    print("Is queue empty?", queue.is_empty())

    # Test delete()
    queue.enqueue(40)
    queue.enqueue(50)
    queue.delete()

    print("After delete:", queue)


if __name__ == "__main__":
    main()