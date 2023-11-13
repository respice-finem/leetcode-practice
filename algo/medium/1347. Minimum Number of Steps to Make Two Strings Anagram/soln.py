def minSteps(s: str, t: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We first get the counts fo the two strings
    2. We then get the difference between s and t to determine how many steps we need to replace
    """
    s_arr = [0] * 26
    t_arr = [0] * 26

    for char in s:
        s_arr[ord(char) - ord('a')] += 1
    for char in t:
        t_arr[ord(char) - ord('a')] += 1

    running_count = 0
    for i in range(26):
        if t_arr[i] > s_arr[i]:
            running_count += t_arr[i] - s_arr[i]
    return running_count 