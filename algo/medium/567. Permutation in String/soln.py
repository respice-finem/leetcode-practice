def checkInclusion(s1: str, s2: str) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We count the number characters in s1
    2. We then have a sliding window size of s1 running through s2. We then keep track of the running count as we slide the window down the character.
    3. If there is a match in the number of characters, we then return 
    """
    if len(s2) < len(s1):
        return False

    running_count = [0] * 26
    s1_count = [0] * 26
    for char in s1:
        s1_count[ord(char)-ord('a')] += 1

    # Build running_count for first n
    for i in range(0, len(s1)):
        running_count[ord(s2[i]) - ord('a')] += 1

    if running_count == s1_count:
        return True

    left = 0
    for i in range(len(s1), len(s2)):
        running_count[ord(s2[left])-ord('a')] -= 1
        running_count[ord(s2[i])-ord('a')] += 1
        if running_count == s1_count:
            return True
        left += 1

    return False