def maxProduct(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    --> Answer from Editorial (Extension of Kadane's Algorithm)
    TODO:
    1. We instantiate 3 different variables to deal with the different scenarios
    2. Idea is that we check the max and mins at each element. The max would either be the current value of the running multiplication or the minimum * negative. If 0, it resets the total and we restart again by checking the current element.
    """
    if len(nums) == 0:
        return 0

    max_so_far = nums[0]
    min_so_far = nums[0]
    result = max_so_far
    
    for i in range(1, len(nums)):
        curr = nums[i]
        temp_max = max(curr, max_so_far * curr, min_so_far * curr)
        min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

        max_so_far = temp_max
        result = max(max_so_far, result)
    return result