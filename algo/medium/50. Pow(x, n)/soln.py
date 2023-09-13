def myPow(x: float, n: int) -> float:
    # NOTE: EDITORIAL ANSWER --> Had issues dealing with the odd and even outcomes
    # NOTE: Revisit and redo
    """
    (Recursive Approach)
    Time Complexity: O(logn)
    Space Complexity: O(logn) --> Call Stack

    TODO:
    1. Iterate through power and divide by 2
    2, Repeat until n becomes 0. If n is currently odd we multiply by x and minus 1 from n
    3. Return output
    """
    def binaryExp(x, n):
        if n == 0:
            return 1

        if n < 0:
            return 1 / binaryExp(x, -1 * n)
        
        if n % 2 == 1:
            return x * binaryExp(x * x, (n-1) // 2)
        else:
            return binaryExp(x * x, n // 2)
    return binaryExp(x, n)


    """
    (Iterative Approach)
    Time Complexity: O(log n)
    Space Complexity: O(1)

    TODO:
    1. Iterate through the power and divide by 2
    2. Repeat until n becomes 0. If n is currently odd we multiply by x and minus 1 from n
    3. Return output
    """
    output = 1
    inverse = n < 0
    n = n * -1 if n < 0 else n

    while n > 0:
        if n % 2 == 1:
            output *= x
            n -= 1
        x *= x
        n //= 2
    return 1 / output if inverse else output