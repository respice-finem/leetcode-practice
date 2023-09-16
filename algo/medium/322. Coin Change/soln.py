from functools import lru_cache

def coinChange(coins: List[int], amount: int) -> int:
    """
    (Top Down)
    --> Look into what lru_cache does, and how does it remove values that are least used
    
    Time Complexity: O(coins * amt)
    Space Complexity: O(amt)

    TODO:
    1. We perform DFS to get the lowest number of coins
    2. Basically we reduce and add the counter by 1, this allows us to keep track of the min cost
    3. Once all possible options have been exhausted, we return the final value
    """

    @lru_cache(None) # Uses a lot of space (Not Optimal and wasteful since we are not reusing our answers)
    def dfs(rem):
        if rem < 0:
            return -1
        if rem == 0:
            return 0
        min_cost = float('inf')
        for coin in coins:
            res = dfs(rem - coin)
            if res != -1:
                min_cost = min(min_cost, res + 1)
        return min_cost if min_cost != float('inf') else -1
    return dfs(amount)

    """
    (Memoization) --> Bottom Up
    Time Complexity: O(coins * amt)
    Space Complexity: O(amt)

    TODO:
    1. We instantiate an empty list to hold all possible amounts
    2. We iterate through the possible combinations
    3. To find the minimum amount of coins we can use, we have to find the min at each point
    """
    combis = [float('inf')] * (amount + 1)
    combis[0] = 0

    for i in range(1, len(combis)):
        for coin in coins:
            temp = i - coin
            if temp >= 0: # Those that are < 0 are not relevant (Shave the search space here)
                combis[i] = min(combis[i], 1 + combis[temp])
    
    return combis[amount] if combis[amount] != float('inf') else -1 