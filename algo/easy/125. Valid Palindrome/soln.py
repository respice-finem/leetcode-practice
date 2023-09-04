def isPalindrome(s: str) -> bool:
    """
    (Suboptimal -- Space-Wise)
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Lower the string
    2. Remove all punctuations and spaces
    3. Reverse and check the string
    """
    s = s.lower()
    s = ''.join([e for e in list(s) if e.isalnum()])
    return s == s[::-1]

    # Cleaner Implementation
    new = ''.join([e.lower() for e in s if e.isalnum()])
    return new == new[::-1]

    """
    (Optimal)
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. Start from two ends
    2. Move inwards and check if they are the same
    3. If not the same, return False
    4. If left == right, we terminate and return True
    """
    left = 0
    right = len(s) - 1
    while left <= right:
        if not s[left].isalnum():
            left += 1
            continue
        elif not s[right].isalnum():
            right -= 1
            continue
        elif s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True