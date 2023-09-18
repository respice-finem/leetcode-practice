def permute(nums: List[int]) -> List[List[int]]:
    """
    Non Swap Method

    Time Complexity: O(n*n!)
    Space Complexity: O(n)

    TODO:
    1. We do a non swap method. We first append the values into our combination, if values have already been seen we skip (ensures unique values)
    2. We repeat until the len of our combi is the same as original then we append and end the checks 
    """
    output = []

    def dfs(combi, seen, cache):
        if len(combi) == len(nums):
            cache.append(combi)
            return
        for num in nums:
            if num not in seen:
                dfs(combi + [num], seen.union(set([num])), cache)
    dfs([], set(), output)
    return output