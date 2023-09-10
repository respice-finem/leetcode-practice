def uniquePaths(m: int, n: int) -> int:
    """
    NOTE:
    There is a math approach that uses combinatorics. Further readings here when I have time:
    https://towardsdatascience.com/understanding-combinatorics-number-of-paths-on-a-grid-bddf08e28384
    """

    """
    (Dynamic Programming Memoization)
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)

    TODO:
    1. We start from the goal
    2. All paths adjacent to the goal would have 1 path
    3. Every other path would be a sum of the down and right paths
    4. We iterate through this and return the total paths at the start
    """
    if m == 1:
        return 1
    output = [[0 for _ in range(n)] for _ in range(m-1)]
    for i in range(len(output) - 1, -1, -1):
        for j in range(len(output[0]) - 1, -1, -1):
            down = output[i+1][j] if i + 1 < len(output) else 1
            right = output[i][j + 1] if j + 1 < len(output[0]) else 0
            output[i][j] = down + right
    return output[0][0]

    """
    (Cleaner Implementation of above)

    Time Complexity: O(m * n)
    Space Complexity: O(n)

    TODO:
    1. Same as method above
    2. We make it cleaner since it reuses the values from the previous row
    3. Therefore, we can keep only one row and update it repeatedly
    """
    output = [1 for _ in range(n)]
    for i in range(m-1):
        for j in range(n-1, -1, -1):
            right = output[j + 1] if j + 1 < n else 0
            output[j] = output[j] + right
    return output[0]