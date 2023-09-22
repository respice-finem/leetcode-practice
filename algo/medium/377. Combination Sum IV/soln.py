from functools import lru_cache

def combinationSum4(nums: List[int], target: int) -> int:
    """
    Memoization (Optimal)

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    TODO:
    NOTE: We can reduce search space by removing values that are unnecessary i.e. larger than target
    1. We instantiate a list of our answers
    2. We do two things when iterating:
    2.5 Add to the current count of vals
    3. Return the index
    """
    nums = [num for num in nums if num <= target]
    ans = [0] * (target + 1)
    ans[0] = 1

    for i in range(1, target+1):
        for num in nums:
            if i - num >= 0:
                ans[i] += ans[i-num]
    return ans[target]

    """
    Backtracking

    Time Complexity: O(n^2)
    Space Complexity: O(n)

    TODO:
    1. We just check if current iteration allows us to get a zero sum
    2. We then increment the count by 1 if it is 0 else we stop searching
    """
    nums = [num for num in nums if num <= target]

    @lru_cache(maxsize=None)
    def dfs(remain):
        if remain == 0:
            return 1
        
        # NOTE: This is how we keep track of our count
        # We keep an interim and run through the options
        # At each level we store the result and output it once completed
        result = 0 
        for num in nums:
            if remain - num >= 0:
                result += dfs(remain - num)
        return result

    return dfs(target)