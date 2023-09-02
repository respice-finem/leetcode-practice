def maxProfit(prices: List[int]) -> int:
    """
    (Suboptimal)

    Time Complexity: O(n^2)
    Space Complexity: O(1)

    TODO:
    1. Iterate through the list twice
    2. Find the pairing that returns the maximunm profit
    """
    curr_max = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            temp = prices[j] - prices[i]
            if temp > curr_max:
                curr_max = temp
    return curr_max

    """
    (Optimal)
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. Iterate through the list
    2. We keep an empty variable to store curr minimum
    2.5 We also keep max profit
    3. If current day yields negative, we discard and use the curr value as new min
    4. Once one pass is over, we return our max profit
    """
    curr_min = prices[0]
    curr_max = 0
    for price in prices:
        if price - curr_min < 0:
            curr_min = price
        else:
            if price - curr_min > curr_max:
                curr_max = price - curr_min
    return curr_max