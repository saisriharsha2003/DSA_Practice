class Node:
    """
    Represents a node in the linked list.
    """

    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    """
    A simple Stack implementation using a singly linked list.

    Stack follows the LIFO (Last In, First Out) principle:
    the last element pushed onto the stack is the first one removed.
    """

    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, item):
        """Add an item to the top of the stack."""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            print("Stack Underflow")
            return
        
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.length -= 1
        return temp.val

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            print("Stack Underflow")
            return
        
        return self.top.val

    def is_empty(self):
        """Return True if the stack contains no elements."""
        return self.length == 0

    def size(self):
        """Return the number of elements currently in the stack."""
        return self.length

    def __str__(self):
        """Return the stack contents as a string."""
        curr = self.top
        res = ""
        while curr:
            res += (str(curr.val) + " -> ")
            curr = curr.next
        return res + "None"


def main():
    """Demonstrate and test basic Stack operations."""

    # Create a new stack
    stack = Stack()

    # Test push()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Display stack
    print("Stack after pushing elements:")
    print(stack)

    # Test peek()
    print("\nTop element:", stack.peek())

    # Test size()
    print("Stack size:", stack.size())

    # Test pop()
    print("\nPopped element:", stack.pop())

    # Display stack after pop
    print("\nStack after pop:")
    print(stack)

    # Test is_empty()
    print("\nIs stack empty?", stack.is_empty())

    # Test remaining pop operations
    print("\nPopped element:", stack.pop())
    print("Popped element:", stack.pop())

    # Test empty stack
    print("\nIs stack empty?", stack.is_empty())

    # Test pop on empty stack
    print("Popped element:", stack.pop())

    # Test peek on empty stack
    print("Top element:", stack.peek())


if __name__ == "__main__":
    main()