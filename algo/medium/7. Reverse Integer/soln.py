def reverse(x: int) -> int:
    """
    (Suboptimal)

    Time Complexity: O(n)
    Space Complexity: O(n)

    TODOL
    1. Convert x into string
    2. Reverse and remove negative if present
    3. Check within bounds
    4. Return output
    """
    temp = str(x)
    nega = temp[0] == "-"
    temp = int(temp[1:][::-1]) * -1 if nega else int(temp[::-1])
    return 0 if temp < -2**31 or temp > 2 ** 31-1 else temp

    """
    (Optimal)
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. Set empty output
    2. Perform the output * 10 + digit
    3. Return negative if needed
    """
    output = 0
    nega = x < 0
    x = -1 * x if nega else x
    while x > 0:
        output = output * 10 + x % 10
        x //= 10
    output = output if not nega else output * -1
    return 0 if output < -2**31 or output > 2 ** 31-1 else output