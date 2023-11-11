def findKthLargest(nums: List[int], k: int) -> int:
    """
    Time Complexity: O(n log n)
    Space Complexity: O(n)

    TODO:
    1. We sort then we get the last kth element
    2. Return the element
    """
    return sorted(nums, reverse=True)[k-1]

    """
    Time Complexity: O(n log k)
    Space Complexity: O(k)

    TODO:
    1. We heapify the nums then we do heappop till we reach k for the length
    2. We then heappop the next one to get the kth largest element
    """
    heapq.heapify(nums)
    while len(nums) > k:
        heapq.heappop(nums)
    return heapq.heappop(nums)

    """
    (QuickSelect)
    Time Complexity: O(n) Amortized
    Space Complexity: O(1)

    TODO:
    1. Method that is used to find kth smallest element. In our case we use it for kth largest, which we will need to tweak a little
    """
    def quick_select(nums, k):
        pivot = random.choice(nums)
        left, mid, right = [], [], []

        for num in nums:
            if num > pivot:
                left.append(num)
            elif num < pivot:
                right.append(num)
            else:
                mid.append(num)

        if k <= len(left):
            return quick_select(left, k)
        if len(left) + len(mid) < k:
            return quick_select(right, k - len(left) - len(mid))
        return pivot
        return quick_select(nums, k) 