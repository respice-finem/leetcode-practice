from collections import deque
class MRUQueue:

    """Unoptimized using list."""
    def __init__(self, n: int):
        self.queue = list(range(1, n+1))

    def fetch(self, k: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)

        In place swaps
        """
        val = self.queue.pop(k-1)
        self.queue.append(val)
        return val

    """Square Root Decomposition."""
    def __init__(self, n: int):
        self.sqrt = ceil(math.sqrt(n))
        self.buckets = []

        nums = list(range(1, n + 1))
        chunks = [nums[i: i + self.sqrt] for i in range(0, len(nums), self.sqrt)]

        for chunk in chunks:
            self.buckets.append(deque(chunk))

    def fetch(self, k: int) -> int:
        """
        Time Complexity: O(n ^ 0.5)
        Space Complexity: O(1)

        TODO:
        1. The idea of square root decomposition is that we reduce the arrays into k ^ 0.5 buckets
        2. We then find the bucket with the index, remove it from the bucket and place it in the last bucket
        3. Starting from the bucket with the removed element, we append the top of the next element and repeat till the end. This is to fill up the gaps. More optimized version of dealing with inserts
        """
        k -= 1
        bucket_idx = k // self.sqrt
        num_idx = k % self.sqrt
        bucket = self.buckets[bucket_idx]
        target_num = bucket[num_idx]

        new_bucket = deque()
        for i, num in enumerate(bucket):
            if i != num_idx:
                new_bucket.append(num)
        self.buckets[bucket_idx] = new_bucket

        self.buckets[-1].append(target_num)

        for b in range(bucket_idx, len(self.buckets) -1):
            left_bucket = self.buckets[b]
            right_bucket = self.buckets[b + 1]
            left_bucket.append(right_bucket.popleft())
        return target_num