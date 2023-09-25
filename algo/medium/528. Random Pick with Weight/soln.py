import random
class Solution:
    """
    My Implementation
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We basically keep tabs and create a cumulative sum of the probabilities
    2. We then do a uniform randon RNG call, we check wherer does this value fall under in the cumu sum
    3. If it is less than the upper boundary and greater than the one before, we return the index

    NOTE: Improvement is to do binary search since it reduces search time to O(log N)
    """

    def __init__(self, w: List[int]):
        self.arr = sorted([[index, weight/sum(w)] for index, weight in enumerate(w)], key=lambda x: x[1])
        running_count = 0
        for e in self.arr:
            running_count += e[1]
            e[1] = running_count

    def pickIndex(self) -> int:
        val = random.random()

        # My Solution (Linear Search)
        # for e in self.arr:
        #     if val <= e[1]:
        #         return e[0]

        # Optimal (Binary Search)
        low, high = 0, len(self.arr)
        while low < high:
            mid = (low + high) // 2
            if val > self.arr[mid][1]:
                low = mid + 1
            else:
                high = mid
        return self.arr[low][0]

    """
    Cleaner Implementation

    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We dont have to sort the array and instead can just run it as it is
    """
    def __init__(self, w: List[int]):
        self.arr = []
        running_count = 0
        for e in w:
            running_count += e
            self.arr.append(running_count)
        self.total = running_count

    def pickIndex(self) -> int:
        val = random.random() * self.total

        # My Solution (Linear Search)
        # for e in self.arr:
        #     if val <= e[1]:
        #         return e[0]

        # Optimal (Binary Search)
        low, high = 0, len(self.arr)
        while low < high:
            mid = (low + high) // 2
            if val > self.arr[mid]:
                low = mid + 1
            else:
                high = mid
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()