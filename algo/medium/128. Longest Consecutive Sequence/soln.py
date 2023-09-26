def longestConsecutive(nums: List[int]) -> int:
    """
    (Unoptimized)
    Time Complexity: O(nlogn)
    Space Complexity: O(n)

    TODO:
    1. Sort and remove the duplicate elements
    2. We then just count running, reset if it's not consecutive
    """
    if len(nums) == 0:
        return 0

    nums = sorted(set(nums))
    running_count = 1
    max_count = 0
    for i in range(1, len(nums)):
        if abs(nums[i] - nums[i-1]) == 1:
            running_count += 1
        else:
            max_count = max(max_count, running_count)
            running_count = 1
    return max(max_count, running_count)

    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    --> Answer from editorial
    --> Similar to what we initially mapped out
    --> But we can do it much elegantly with a hashset

    TODO:
    1. We first create a set of our current nums
    2. We check if our number has a head i.e. if n-1 is in the set. If not we can ensure that this is a unique start and won't be part of another sequence
    3. We then iterate upwards and get the max length
    4. We then return  the maximum streak
    """
    max_count = 0
    nums = set(nums)

    for num in nums:
        if num - 1 not in nums:
            temp = num
            running_count = 1
            while temp + 1 in nums:
                temp += 1
                running_count += 1
            max_count = max(running_count, max_count)
    return max_count