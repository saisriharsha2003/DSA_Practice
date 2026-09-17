class Stack:
    """
    A simple Stack implementation using a Python list.

    Stack follows the LIFO (Last In, First Out) principle:
    the last element pushed onto the stack is the first one removed.
    """

    def __init__(self):
        # Initialize an empty list to store stack elements
        self.stack = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.stack.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            return "Stack Underflow"

        return self.stack.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            return "Stack is empty"

        return self.stack[-1]

    def is_empty(self):
        """Return True if the stack contains no elements."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of elements currently in the stack."""
        return len(self.stack)

    def __str__(self):
        """
        Return the stack contents as a string.

        The top element is displayed first.
        """
        if self.is_empty():
            return "Stack is empty"

        # Reverse the list so that the top of the stack is displayed first
        values = [str(x) for x in reversed(self.stack)]
        return "\n".join(values)


def main():
    """Demonstrate basic Stack operations."""

    # Create a new stack
    stack = Stack()

    # Add elements to the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack after pushing elements:")
    print(stack)

    # Check the top element without removing it
    print("\nTop element:", stack.peek())

    # Check the number of elements
    print("Stack size:", stack.size())

    # Remove the top element
    print("\nPopped element:", stack.pop())

    print("\nStack after pop:")
    print(stack)

    # Check if the stack is empty
    print("\nIs stack empty?", stack.is_empty())


# Execute main() only when this file is run directly
if __name__ == "__main__":
    main()
