def minimumTotal(triangle: List[List[int]]) -> int:
    """
    Bottom Up
    Time Complexity: O(n * k)
    Space Complexity: O(1)

    TODO:
    1. We keep the index and perform the addition from bottom up
    2. At each level we then return the minimum, and move on
    3. Return the last digit at the top which will give the negative
    """
    for i in range(len(triangle)-1, 0, -1): # Each Level we check previous
        for j in range(len(triangle[i-1])):
            triangle[i-1][j] = min(triangle[i-1][j] + triangle[i][j], triangle[i-1][j] + triangle[i][j+1])
    return triangle[0][0]

    """
    Top Down
    Time Complexity: O(n * k)
    Space Complexity: O(1)
    --> Answer from Editorial

    TODO:
    1. We do similar to above but from the top down
    """
    for row in range(1, len(triangle)):
        for col in range(row+1):
            smallest_above = math.inf
            if col > 0:
                smallest_above = triangle[row - 1][col - 1]
            if col < row:
                smallest_above = min(smallest_above, triangle[row - 1][col])
            triangle[row][col] += smallest_above
    return min(triangle[-1])