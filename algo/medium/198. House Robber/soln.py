def rob(nums: List[int]) -> int:
    """
    Time Complexity: O(n ^ 2)
    Space Complexity: O(n)
    NOTE: Optimized Brute Force
    TODO:
    1. We first do skips and add. We then do max(max(curr_running_arr, nums[i]) + nums[j] ,curr_running_arr)
    2. We then get the max of the tabulated output
    """
    arr = list(nums)

    for i in range(len(nums)):
        for j in range(i + 2, len(nums)):
            arr[j] = max(max(nums[i], arr[i]) + nums[j], arr[j])
    return max(arr)

    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. The idea of this bottom up is that at each point, we can check if we rob from i-2 and current against the i - 1, which captures what we want to achieve above
    2. We would then return the end index to achieve the max output
    # """
    rob1, rob2 = 0, 0

    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2