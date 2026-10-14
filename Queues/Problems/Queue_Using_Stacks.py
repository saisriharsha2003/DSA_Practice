class Stack:
    def __init__(self):
        self.stack = []
        self.l = 0

    def push(self, x):
        self.stack.append(x)
        self.l += 1

    def pop(self):
        if self.l == 0:
            return "Queue Underflow"
        else:
            self.l -= 1
            return self.stack.pop() 

    def __len__(self):
        return self.l    

    def peek(self):
        if self.l == 0:
            return "Queue Underflow"
        else:
            return self.stack[-1]

    def isEmpty(self):
        return self.l ==0
        
class MyQueue:
    def __init__(self):
        self.instack = Stack()
        self.outstack = Stack()

    def push(self, x):
        self.instack.push(x)

    def pop(self):
        if len(self.outstack) == 0:
            while len(self.instack) > 0:
                self.outstack.push(self.instack.pop())
        
        res = self.outstack.pop()
        return res 

    def peek(self):
        if len(self.outstack) == 0:
            while len(self.instack) > 0:
                self.outstack.push(self.instack.pop())
        return self.outstack.peek()


    def empty(self):
        return self.instack.isEmpty() and self.outstack.isEmpty()


def main():
    queue = MyQueue()

    queue.push(1)
    queue.push(2)
    queue.push(3)

    print("Front:", queue.peek())       # Expected: 1
    print("Removed:", queue.pop())      # Expected: 1
    print("Front after pop:", queue.peek())  # Expected: 2

    queue.push(4)

    print("Removed:", queue.pop())      # Expected: 2
    print("Removed:", queue.pop())      # Expected: 3
    print("Is empty?", queue.empty())   # Expected: False

    print("Removed:", queue.pop())      # Expected: 4
    print("Is empty?", queue.empty())   # Expected: True


if __name__ == "__main__":
    main()
