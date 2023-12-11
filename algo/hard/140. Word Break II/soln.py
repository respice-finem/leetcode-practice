 def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    """
    Time Complexity:
    Space Complexity:

    TODO:
    1. We use the approach in Word Break I to setup up our values. However, instead of setting up the True or False, we can build our values accordingly based on the previous values
    2. Once we reach the last value, we can just return the final output
    """
    dp = [[]] * len(s)

    for i in range(len(s)):
        for word in wordDict:
            if i < len(word) - 1:
                continue
            if i == len(word) - 1 or dp[i - len(word)]:
                if s[i-len(word)+1: i + 1] == word:
                    if i - len(word) > -1 and dp[i-len(word)]:
                        temp = [e + [word] for e in dp[i - len(word)]]
                    else:
                        temp = [[word]]
                    if dp[i]:
                        dp[i] += temp
                    else:
                        dp[i] = temp

    return [' '.join(e) for e in dp[-1]]