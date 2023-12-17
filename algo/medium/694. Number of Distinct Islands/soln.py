def numDistinctIslands(self, grid: List[List[int]]) -> int:
    """
    Time Complexity: O(m * n)
    Space Complexity: O(n)

    TODO:
    1. We do a DFS and keep track of the direction that it takes and when all has been visited, we return the path
    2. If path has been seen before, we skip else we append to the set. We have to take care of an edge case which is when it is singular we give a starting character to indicate it is valid
    3. Return the length
    """
    r, c = len(grid), len(grid[0])
    paths = set()
    def dfs(x, y, node_num):
        grid[x][y] = 'v'
        for loc, coord, num_change in [
            ['U', (-1,0), -c], ['D', (1,0), c], ['L', (0,-1), -1], ['R', (0,1), 1]
        ]:
            if -1 < (x + coord[0]) < r and -1 < (y + coord[1]) < c \
            and grid[x + coord[0]][y + coord[1]] == 1:
                new_node = node_num + num_change
                curr_path.append(str(node_num) + loc)
                dfs(x + coord[0], y + coord[1], new_node)
    
    for i in range(r):
        for j in range(c):
            curr_path = []
            if grid[i][j] == 1:
                curr_path.append("*")
                dfs(i, j, 0)
            curr_path = ''.join(curr_path)
            if curr_path:
                paths.add(curr_path)
    return len(paths)