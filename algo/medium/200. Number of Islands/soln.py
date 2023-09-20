def numIslands(grid: List[List[str]]) -> int:
    """
    BFS Approach
    Time Complexity: O(m * n)
    Space Complexity: O(1) --> Reusing the grid without creating a seen

    TODO:
    1. We do a BFS for 1s and mark them with V if it is visited
    2. Once done we increment count by 1
    3. Once we run out of 1s, we return the output
    """
    r, c = len(grid), len(grid[0])
    output = 0
    
    def bfs(sr, sc):
        queue = deque()
        queue.append((sr, sc))
        
        while queue:
            x0, y0 = queue.popleft()
            for x, y in [(-1,0), (1,0), (0,1), (0,-1)]:
                x1, y1 = x + x0, y + y0
                if -1 < x1 < r and -1 < y1 < c and grid[x1][y1] != 'v':
                    if grid[x1][y1] == "1":
                        queue.append((x1, y1))
                        grid[x1][y1] = "v"
        return 1

    for i in range(r):
        for j in range(c):
            if grid[i][j] == "1":
                output += bfs(i, j)
    return output

    """
    DFS Approach

    Time Complexity: O(m * n)
    Space Complexity: O(m * n) --> Call Stack

    TODO:
    1. Same as above but instead of BFS we do DFS
    """
    r, c = len(grid), len(grid[0])
    output = 0
    
    def dfs(sr, sc):
        if grid[sr][sc] == 0:
            return
        grid[sr][sc] = 'v'
        for x, y in [(-1,0), (1,0), (0,1), (0,-1)]:
            x1, y1 = x + sr, y + sc
            if -1 < x1 < r and -1 < y1 < c and grid[x1][y1] != 'v':
                if grid[x1][y1] == "1":
                    dfs(x1, y1)
        return 1

    for i in range(r):
        for j in range(c):
            if grid[i][j] == "1":
                output += dfs(i, j)
    return output