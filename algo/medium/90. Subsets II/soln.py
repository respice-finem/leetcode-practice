def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    """
    Time Complexity: O(n * 2^n)
    Space Complexity: O(1)

    TODO:
    1. We generate an empty set and store our values there for values that have been seen
    2. We then add the current nums to the existing output and check if it has already been seen. If not we append to output
    3. Return the output
    """
    nums = sorted(nums)
    output = [[]]

    for num in nums:
        arr = []
        for val in output:
            temp = val + [num]
            if temp not in output:
                arr.append(temp)
        output += arr
    return output

    """
    Time Complexity: O(n*2^n)
    Space Complexity: O(1)

    TODO:
    1. Same as above but recursive
    """
    nums = sorted(nums)
    def dfs(curr, start):
        if len(nums) == 0:
            return
        for i in range(start, len(nums)):
            temp = curr + [nums[i]]
            if temp not in output:
                output.append(temp)
                dfs(temp, i+1)
    output = [[]] # Containers are fine to be global variables for recursive functions
    dfs([], 0)
    return  output