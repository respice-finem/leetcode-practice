from collections import deque

def orangesRotting(grid: List[List[int]]) -> int:
    """
    BFS + Two Pass

    Time Complexity: O(m * n)
    Space Complexity O(m * n)

    TODO:
    1. Copy the grid and convert all the 1s to infinite while the rest would be 0
    2. Collect all the rotten oranges indexes
    3. For each rotten we run a BFS and calculate the minimum time taken for it to be turnt to rotten versus the current minimum
    4. Get the max value in the copied grid
    """
    r, c = len(grid), len(grid[0])
    grid_copy = [[0 if grid[i][j] != 1 else float('inf') for j in range(c)] for i in range(r)]
    queue = deque()

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 2:
                queue.append((i, j, 0))

    while queue:
        x0, y0, steps = queue.popleft()
        for x, y in [(-1,0), (1,0), (0,1), (0,-1)]:
            x1, y1 = x + x0, y + y0
            if -1 < x1 < r and -1 < y1 < c:
                if grid[x1][y1] == 1:
                    if grid_copy[x1][y1] > steps + 1:
                        grid_copy[x1][y1] = steps + 1
                        queue.append((x1, y1, steps + 1))

    maxi_output = 0
    for i in range(r):
        for j in range(c):
            if grid_copy[i][j] > maxi_output:
                maxi_output = grid_copy[i][j]

    return maxi_output if maxi_output != float('inf') else -1