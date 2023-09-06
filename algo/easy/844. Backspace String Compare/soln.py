def backspaceCompare(s: str, t: str) -> bool:
    """
    (Suboptimal)
    Time Complexity: O(s + t) --> Two Pass
    Space Complexity: O(s + t)

    TODO:
    1. Create two empty stacks
    2. Iterate through two strings
    3. Append if alnum, pop if #
    4. Compare both stacks once completed
    """
    s1 = []
    s2 = []

    for char in s:
        if char.isalnum():
            s1.append(char)
        else:
            if s1:
                s1.pop()
            else:
                continue
    
    for char in t:
        if char.isalnum():
            s2.append(char)
        else:
            if s2:
                s2.pop()
            else:
                continue
    return s1 == s2

    """
    (Optimal)
    --> Should be Medium
    --> Editorial Solution is not O(1) Space
    Refer to: https://leetcode.com/problems/backspace-string-compare/solutions/585027/python-o-n-time-o-1-space-solution-explained/

    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. Start from behind for both arrays
    2. We iterate through both the arrays
    3. For both arrays, we check how many times we need to backspace
    4. Perform backspace and compare the elements
    5. If elements are not the same, we return False
    """
    i_s = len(s) - 1
    i_t = len(t) - 1

    skip_s = 0
    skip_t = 0

    while i_s >= 0 or i_t >= 0:
        while i_s >= 0:
            if s[i_s] == "#":
                skip_s += 1
                i_s -= 1
            elif skip_s > 0:
                skip_s -= 1
                i_s -= 1
            else:
                break # Stop if there no more "#"

        while i_t >= 0:
            if t[i_t] == "#":
                skip_t += 1
                i_t -= 1
            elif skip_t > 0:
                skip_t -= 1
                i_t -= 1
            else:
                break # Stop if there no more "#"
        
        if i_s >= 0 and i_t >= 0 and s[i_s] != t[i_t]:
            return False

        if (i_s >= 0) != (i_t >= 0):
            return False

        i_s -= 1
        i_t -= 1

    return True