class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        if not self.s1:
            self.s1.append(x)
        else:
            self.s2.append(x)

    def pop(self) -> int:
        temp = self.s1.pop() # Time Complexity: O(1) if not empty
        if not self.s1:
            while self.s2:
                self.s1.append(self.s2.pop()) # Amortized here. Refills if needed
        return temp

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()