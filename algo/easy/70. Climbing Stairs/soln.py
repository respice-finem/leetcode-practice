def climbStairs(n: int) -> int:
    """
    Memoization
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. As we can reuse the previous answers to get our next values, we save the answer in an array with length n
    2. We then return the value at n
    """
    output = [0] * (n + 1)
    output[0] = 1
    output[1] = 1

    for i in range(2, n+1):
        output[i] = output[i - 1] + output[i - 2]
    return output[n]
    
    """
    Fibonacci
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. If we observe closely the pattern follows a fibonacci pattern. Thus, we only need to store the last known number
    2. This cuts down the space used
    """
    prev, curr = 1, 1

    for i in range(1, n):
        temp = curr 
        curr = prev + curr
        prev = temp
    return curr