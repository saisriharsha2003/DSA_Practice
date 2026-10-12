class PriorityQueue:
    """
    A Priority Queue implementation.

    Elements are removed according to their priority.
    Smaller priority number means higher priority.
    """

    def __init__(self):
        """Initialize an empty priority queue."""
        self.queue = []

    def enqueue(self, item, priority):
        """Add an item with its priority."""
        self.queue.append((priority, item))

    def dequeue(self):
        """Remove and return the highest-priority item."""
        if self.is_empty():
            return "Queue Underflow"
        
        high_p = 0
        for i in range(1, len(self.queue)):
            if self.queue[high_p][0] >= self.queue[i][0]:
                high_p = i
        
        return self.queue.pop(high_p)[1]

    def peek(self):
        """Return the highest-priority item without removing it."""
        if self.is_empty():
            return "Queue is Empty"
        
        high_p = 0
        for i in range(1, len(self.queue)):
            if self.queue[high_p][0] >= self.queue[i][0]:
                high_p = i
        
        return self.queue[high_p][1]

    def is_empty(self):
        """Return True if the priority queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of elements in the priority queue."""
        return len(self.queue)

    def delete(self):
        """Delete all elements from the priority queue."""
        self.queue = []

    def __str__(self):
        """Return string representation of the priority queue."""
        if self.is_empty():
            return "Queue is empty"
        
        return str(self.queue)


def main():
    """Demonstrate and test the Priority Queue."""

    queue = PriorityQueue()

    # Test enqueue()
    queue.enqueue("Task A", 3)
    queue.enqueue("Task B", 1)
    queue.enqueue("Task C", 2)

    # Test __str__()
    print("Priority Queue:", queue)

    # Test peek()
    print("Highest-priority item:", queue.peek())

    # Test dequeue()
    print("Dequeued item:", queue.dequeue())

    # Test size()
    print("Queue size:", queue.size())

    # Test remaining items
    print("Dequeued item:", queue.dequeue())
    print("Dequeued item:", queue.dequeue())

    # Test empty queue
    print("Dequeued item:", queue.dequeue())
    print("Is queue empty?", queue.is_empty())


if __name__ == "__main__":
    main()