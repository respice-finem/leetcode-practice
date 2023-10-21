def minPathSum(grid: List[List[int]]) -> int:
    """
    Time Complexity: O(m*n)
    Space Complexity: O(1)

    TODO:
    1. We count the down and right starting from the lowest
    2. We then fill up the values in the matrix
    3. Return matrix[0][0]
    """
    for i in range(len(grid)-1,-1,-1):
        for j in range(len(grid[i])-1, -1, -1):
            if i == len(grid)-1 and j == len(grid[i])-1:
                continue
            elif j == len(grid[i]) - 1:
                grid[i][j] += grid[i+1][j]
            elif i == len(grid)-1:
                grid[i][j] += grid[i][j+1]
            else:
                down = grid[i+1][j]
                right = grid[i][j+1]
                grid[i][j] = min(grid[i][j]+down, grid[i][j]+right)
    return grid[0][0] 