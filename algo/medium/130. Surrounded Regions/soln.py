from collections import deque

def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    """
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)

    TODO:
    1. We check from the boundaries and if it is O we do a DFS/BFS to check for any O in the path. If there is any O seen in path, we then store the seen in index
    2. Once that's done, we check for those O that are not in seen as X.
    """
    row, col = len(board), len(board[0])
    seen = set()
    
    def dfs(r, c):
        seen.add((r, c))
        for x, y in [(-1,0), (1,0), (0, 1), (0, -1)]:
            if board[r][c] == 'O' and -1 < r + x < row and -1 < c + y < col and (r + x, c + y) not in seen:
                dfs(r + x, c + y)

    for i in range(row):
        if i in [0, row - 1]:
            for j in range(col):
                if board[i][j] == 'O':
                    dfs(i , j)
        else:
            for j in [0, col - 1]:
                if board[i][j] == 'O':
                    dfs(i , j)
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'O' and (i, j) not in seen:
                board[i][j] = 'X'