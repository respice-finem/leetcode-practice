def exist(board: List[List[str]], word: str) -> bool:
    """
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    --> NOTE: Need to look at this again
    TODO:
    1. DFS on letters that matches the start
    2. Recur until we get a match. Propagate the values upwards
    """
    r, c = len(board), len(board[0])

    def dfs(remain, x0, y0):
        if not (-1 < x0 < r and -1 < y0 < c) or remain[0] != board[x0][y0]:
            return
        elif len(remain) == 1 and remain[0] == board[x0][y0]:
            return True
        
        for x, y in [(-1,0), (1,0), (0,1), (0, -1)]:
            x1, y1 = x + x0, y + y0
            if board[x0][y0] == remain[0] and (x1, y1) not in seen:
                seen.add((x0, y0))
                if dfs(remain[1:], x1, y1):
                    return True
                seen.remove((x0, y0))
        return False
    for i in range(r):
        for j in range(c):
            seen = set()
            if board[i][j] == word[0]:
                if dfs(word, i, j):
                    return True