class MyQueue:

    def __init__(self):
        self.main_stack = []
        self.assistant_stack = []

    def push(self, x: int) -> None:
        while len(self.main_stack) > 0:
            self.assistant_stack.append(self.main_stack[-1])
            self.main_stack.pop()
        self.main_stack.append(x)
        while len(self.assistant_stack) > 0:
            self.main_stack.append(self.assistant_stack[-1])
            self.assistant_stack.pop()

    def pop(self) -> int:
        res = self.main_stack[-1]
        self.main_stack.pop()
        return res

    def peek(self) -> int:
        return self.main_stack[-1]

    def empty(self) -> bool:
        return len(self.main_stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()