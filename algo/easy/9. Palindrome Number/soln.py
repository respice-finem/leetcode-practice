def isPalindrome(x: int) -> bool:
    """
    (Suboptimal)

    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Convert to string
    2. Return if reverse and normal are the same
    """
    return str(x) == str(x)[::-1]

    """
    One Pass

    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We get number of 10s we need to subtract
    2. Then we rebuild by taking the remainder and adding to the value
    3. Return If rebuilt value is equal to ori
    """
    output = 0
    temp = x
    while x > 0:
        output = output * 10 + x % 10 # Important so that we dont have to count how many tens we need
        x //= 10
    return output == temp