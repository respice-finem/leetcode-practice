from collections import deque

class HitCounter:
    """
    Time Complexity: O(1) Amortized
    Space Complexity: O(n)

    TODO:
    1. When we hit, we just append
    2. When we getHits, we pop what we do not need and return the length
    --> Costly if it is a huge list since we need to pop a lot
    """

    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0] <= timestamp - 300: # Amortized call
            self.hits.popleft() # This works because assumption is that calls are made in chronological order
        return len(self.hits)

    """
    Time Complexity: O(1) Amortized
    Space Complexity: O(n)

    TODO:
    1. When we hit, we just append but condense it so that we would remove redundant calls
    2. When we getHits, we pop what we do not need and return the length
    (Slightly more optimized)
    """
    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        # Good method to combine repeated inputs as a block so that we reduce the amount of operations
        # For pops
        if not self.hits:
            self.hits.append([timestamp, 1])
        else:
            if self.hits[-1][0] == timestamp:
                self.hits[-1][1] += 1
            else:
                self.hits.append([timestamp, 1])

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0][0] <= timestamp - 300:
            self.hits.popleft()
        return sum([e[1] for e in self.hits])

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)