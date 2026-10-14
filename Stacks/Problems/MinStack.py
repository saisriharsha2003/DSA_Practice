
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MinStack:
    def __init__(self):
        self.top = None
        self.minNode = None

    def push(self, val: int) -> None:
        self.top = Node(val, self.top)

        if self.minNode is None or val <= self.minNode.val:
            self.minNode = Node(val, self.minNode)

    def pop(self) -> None:
        if self.top.val == self.minNode.val:
            self.minNode = self.minNode.next

        self.top = self.top.next

    def topValue(self) -> int:
        return self.top.val

    def getMin(self) -> int:
        return self.minNode.val


def main():
    stack = MinStack()

    stack.push(5)
    stack.push(3)
    stack.push(3)
    stack.push(7)
    stack.push(2)

    print(stack.topValue())  # 2
    print(stack.getMin())    # 2

    stack.pop()
    print(stack.topValue())  # 7
    print(stack.getMin())    # 3

    stack.pop()
    stack.pop()
    print(stack.getMin())    # 5


if __name__ == "__main__":
    main()
