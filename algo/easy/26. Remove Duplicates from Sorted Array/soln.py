def removeDuplicates(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. Keep two pointers (left and right) and move right until we get a new value
    2. If we get new value, we then replace the left and increment left by 1.
    """
    left, right = 1, 1
    curr = nums[0]
    while right < len(nums):
        if curr != nums[right]:
            nums[left] = nums[right]
            curr = nums[left]
            left += 1
        right += 1
    return left