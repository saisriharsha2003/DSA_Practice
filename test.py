class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MinStack:

    def __init__(self):
        self.top = None
        self.minNode = None

    def push(self, val: int) -> None:
        self.top = Node(val = val, next = self.top)
        if (self.minNode is None) or (self.minNode.val >= val):
            self.minNode = Node(val = val, next = self.minNode)

    def pop(self) -> None:
        if self.top.val == self.minNode.val:
            self.minNode = self.minNode.next
        self.top = self.top.next

    def peek(self) -> int:
        return self.top.val

    def getMin(self) -> int:
        return self.minNode.val


def main():
    min_stack = MinStack()

    # Push values, including duplicate minimums
    min_stack.push(5)
    min_stack.push(3)
    min_stack.push(3)

    print("Current minimum:", min_stack.getMin())  # 3

    min_stack.pop()
    print("After first pop:")
    print("Top:", min_stack.peek())                # 3
    print("Minimum:", min_stack.getMin())          # 3

    min_stack.pop()
    print("After second pop:")
    print("Top:", min_stack.peek())                # 5
    print("Minimum:", min_stack.getMin())          # 5


if __name__ == "__main__":
    main()
