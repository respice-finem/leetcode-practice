def maxSubArray(nums: List[int]) -> int:
    """
    (Two Pass)
    ---> Kadane's Algorithm when it comes to getting maximum subarrays (Intuition is in the TODO)
    NOTE: Practice more on related questions
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. Calculate a cumulative sum of the nums
    2. If the current sum is lower than 0, we check if which one is larger. We can then append to that point and reset the sum since anyting before that will not be greater. We can then recalculate the sum
    3. We then iterate through and get the max value
    """
    if len(nums) == 1:
        return nums[0]

    temp = 0
    for i in range(len(nums)):
        temp += nums[i]
        if temp < 0:
            temp = max(nums[i], temp)
            nums[i] = temp
            temp = 0
        else:
            nums[i] = temp
    return max(nums)