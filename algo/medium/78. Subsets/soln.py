def subsets(nums: List[int]) -> List[List[int]]:
    """
    (Top Down)
    Time Complexity: O(n * 2 ^ n)
    Space Complexity: O(n * 2 ^ n)

    TODO:
    1. We can do a DFS to check if we done it before
    2. Return the output
    """
    output = [[]]

    def dfs(nums, curr_set, output):
        if not nums: # Base Case
            return
        for i in range(len(nums)):
            temp = curr_set + [nums[i]]
            output.append(temp)
            dfs(nums[i+1:], temp, output)
    
    dfs(nums, [], output)
    return output

    """
    (Memoization)
    --> Important to know how to use (Power Set, good for determining combinations)
    Time Complexity: O(n * 2n)
    Space Complexity: O(n * 2 ^ n)

    TODO:
    1. We reuse our values to generate new subsets
    """
    output = [[]]

    for num in nums:
        temp = []
        for vals in output:
            temp.append(vals + [num])
        output += temp
    return output