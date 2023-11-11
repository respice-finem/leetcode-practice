def lengthOfLongestSubstring(s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We keep a sliding window, if elements are found in hash set, we remove what was in the seen and move our left pointer forward until we see a unique character
    2. Check for max length at each point and return max length once the right pointer reaches the end
    """

    if len(s) == 0:
        return 0

    left, right = 0, 1
    seen = set([s[0]])
    max_length = 1
    while right < len(s):
        if s[right] in seen:
            seen.remove(s[left])
            left += 1
        else:
            seen.add(s[right])
            right += 1
            max_length = max(max_length, right - left)
    return max_length