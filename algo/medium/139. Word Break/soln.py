def wordBreak(s: str, wordDict: List[str]) -> bool:
    """
    Time Complexity: O(n * m * k)
    Space Complexity: O(n) --> Call Stack
    NOTE: Top Down
    TODO:
    1. We create an array that keeps track of the possible words
    2. We then do a DFS to search the value with cache
    """
    chars = {i: [] for i in range(26)}
    for word in wordDict:
        chars[ord(word[0])-ord('a')].append(word)

    @cache
    def dfs(s, curr_index):
        if curr_index >= len(s):
            return True
        output = False
        temp_index = ord(s[curr_index]) - ord('a')
        for curr_word in chars[temp_index]:
            if curr_word == s[curr_index: curr_index + len(curr_word)]:
                output = dfs(s, curr_index + len(curr_word))
            if output:
                return True
        return output
    return dfs(s, 0)

    """
    Time Complexity: O(n * m * k)
    Space Complexity: O(n)
    NOTE: Answer from editorial, we can refine our code above by only checking if we at each point

    TODO:
    1. Same as above but we do it iteratively from the bottom up
    2. Smart way to check for pointers which it can be built from, this way we do not have to keep iterating
    """
    dp = [False] * len(s)
    for i in range(len(s)):
        for word in wordDict:
            # Out of bounds
            if i < len(word) - 1:
                continue
            # i == len(word) - 1, checks for starters
            # dp[i - len(word)] can the word be built from there
            if i == len(word) - 1 or dp[i - len(word)]:
                if s[i - len(word) + 1: i + 1] == word:
                    dp[i]= True
                    break
    return dp[-1]