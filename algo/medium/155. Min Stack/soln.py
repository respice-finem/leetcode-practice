class MinStack:
    """
    Stack of Value and Min Pairs
    
    Time Complexity: O(1)
    Space Complexity: O(n)

    TODO:
    1. We push our values in as a value and min pair
    2. This continuously keeps track of our min at each point
    3. As such we can keep our time complexity constant
    """

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
        else:
            if val < self.getMin():
                self.stack.append(
                    [val, val]
                )
            else:
                self.stack.append(
                    [val, self.getMin()]
                )

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

    """
    (Two Stacks)

    Time Complexity: O(1)
    Space Complexity: O(n)
    
    TODO:
    1. Idea is same as above, but we split the pairs into a two stack
    2. We input the main value in first stack and minimum in second stack
    3. When we pop we remove in both stacks
    NOTE:
    There is a more elegant way of storing the mins in stack2.
    I.e. we store it as (mins, count), if the new min is lower we insert new else update.
    Pop only when count is 0 (More steps but easier to debug IRL)
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val: int) -> None:
        if not self.stack1 and not self.stack2:
            self.stack1.append(val)
            self.stack2.append(val)
        else:
            if val < self.getMin():
                self.stack2.append(val)
            else:
                self.stack2.append(self.getMin())
            self.stack1.append(val)

    def pop(self) -> None:
        self.stack1.pop()
        self.stack2.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.stack2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()