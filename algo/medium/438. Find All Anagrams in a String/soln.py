def findAnagrams(s: str, p: str) -> List[int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We keep two arrays of all alphabets
    2. We do a count of the alphabets for p
    3. We then do a sliding window starting from the first len(p) words and count. Everytime we move down, we + and - the relevant alphabet count and compare. If the arrays are the same, we append the index
    4. Return the index array
    """
    p_counts = [0] * 26
    s_counts = [0] * 26
    output = []

    for char in p:
        p_counts[ord(char)-ord('a')] += 1

    for char in s[:len(p)]:
        s_counts[ord(char)-ord('a')] += 1
    if s_counts == p_counts:
        output.append(0)

    for i in range(len(p), len(s)):
        s_counts[ord(s[i - len(p)])-ord('a')] -= 1
        s_counts[ord(s[i])-ord('a')] += 1
        if s_counts == p_counts:
            output.append(i - len(p) + 1)
    return output

    """
    (Suboptimal)
    Time Complexity: O(n * klogk)
    Space Complexity: O(1)

    TODO:
    1. For each substring, we sort the valeus and compare against the sorted p
    2. If is the same we append the index
    3. Return the intended value 
    """
    output = []
    p = sorted(p)

    for i in range(len(s)-len(p)+1):
        if sorted(s[i:i+len(p)]) == p:
            output.append(i)
    return output