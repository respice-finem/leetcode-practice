def longestCommonPrefix(strs: List[str]) -> str:
    # NOTE: We have a binary search method and also a recursive split method
    # Though we do not gain any extra benefits in terms of Time Complexity
    # Good to revisit
    
    """
    (Horizonal Scanning)
    Time Complexity: O(n * K)
    Space Complexity: O(K)

    TODO:
    1. We basically take the first word then compare against all words
    2. If different we remove up till the letter before it was different. If length is shorter then we stop at where the word ends
    """
    prefix = strs[0]

    for i in range(1, len(strs)):
        right = 0
        while right < min(len(strs[i]), len(prefix)):
            if strs[i][right] != prefix[right]:
                break
            right += 1
        prefix = prefix[:right]
    return prefix

    """
    Vertical Scanning
    Time Complexity: O(n * k)
    Space Complexity: O(1)
    ---> Answer from editorial

    TODO:
    1. We go through each element and build the prefix
    2. We stop once one of them are different
    """
    if not str:
        return ""

    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][:i]
    return strs[0]