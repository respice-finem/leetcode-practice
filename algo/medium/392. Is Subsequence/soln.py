def isSubsequence(s: str, t: str) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    Two Pointer Approach

    TODO:
    1. We start from 0 as pointer for both s and t 
    2. Since it is a subsequence, all we have to do is move the pointer on s everytime we see a val in t
    3. If the left pointer is equal to the length of s, then we return True else Flase
    """
    left = right = 0

    while left < len(s) and right < len(t):
        if s[left] == t[right]:
            left += 1
        right += 1
    return left == len(s)

    """
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    --> Answer from Editorial (More on the Edit Distance Question DP)

    TODO:
    1. The idea is that we create a prefix matrix to determine how many characters
    2. We then check if we can get a match we then add a value at that index
    3. We then return if we fully found the match
    """
    len_s, len_t = len(s), len(t)

    if len_s == 0:
        return True

    dp = [[0] * (len_t + 1) for _ in range(len_s + 1)]

    for col in range(1, len_t + 1):
        for row in range(1, len_s + 1):
            if s[row - 1] == t[col-1]:
                dp[row][col] = dp[row-1][col-1] + 1
            else:
                dp[row][col] = max(dp[row][col-1], dp[row-1][col]) # Get max number of matches so far
        if dp[len_s][col] == len_s:
            return True

    return False