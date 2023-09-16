def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    """
    (Simulation Approach)
    Time Complexity: O(n * n)
    Space Complexity: O(1)

    TODO:
    1. Since it works somewhat similar to a spiral, we do a four place swap at each iteration
    2. We then shrink the boundaries for each swap
    """
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        for j in range(i, col-i-1):
            matrix[i][j], matrix[j][col-1-i], matrix[row-1-i][col-1-j], matrix[row-j-1][i] = matrix[row-j-1][i], matrix[i][j], matrix[j][col-1-i], matrix[row-1-i][col-1-j]

    """
    (Math Approach)
    ---> Answer from editorial
    Time Complexity: O(n * n)
    Space Complexity: O(1)

    TODO:
    1. 90 degree rotation is the same as a reflection and reversal
    2. Therefore, we can do that in code
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]