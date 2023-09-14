class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(timestamp, value)]
        else:
            self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        # NOTE: Draw out logic to internalize this
        Time Complexity: O(log n)
        Space Complexity: O(1)

        TODO:
        1. The logic is similar to using binary search to find where to make our inserts
        2. At each mid point we check if target timestamp is greater than the timestamp at the mid index
        3. If it is, we continue searching by looking at the space to the right of the mid index
        4. If it is not, we search the space to the left since the mid index is not what we are looking for
        5. We will eventually converge to a point where it is the largest value that is <= target timestamp.
        """
        arr = self.map.get(key, [])
        if not arr:
            return ''
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid][0] <= timestamp:
                start = mid + 1
            else:
                end = mid - 1
        return arr[end][1] if end != -1 else ''
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)