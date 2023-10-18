from collections import deque

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We search for the 1 index then perform a BFS.
    2. We then get the length of seen to update the count
    """
    r,c = len(grid), len(grid[0])
    def bfs(x0, y0):
        queue = deque()
        queue.append((x0, y0))
        seen = set()
        seen.add((x0, y0))

        while queue:
            curr_x, curr_y = queue.popleft()
            for x, y in [(-1,0), (1,0), (0,1), (0,-1)]:
                x1, y1 = curr_x + x, curr_y + y
                if -1 < x1 < r and -1 < y1 < c and (x1, y1) not in seen:
                    if grid[x1][y1] == 1:
                        queue.append((x1, y1))
                        seen.add((x1, y1))
                        grid[x1][y1] = 'v'

        return len(seen)
    max_area = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                max_area = max(max_area, bfs(i, j))
    return max_area

    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Similar as above but we do DFS
    """
    r,c = len(grid), len(grid[0])
    def dfs(x0, y0):
        stack = [(x0, y0)]
        seen = set()
        seen.add((x0, y0))
        area = 0
        while stack:
            curr_x, curr_y = stack.pop()
            area += 1
            for x, y in [(-1,0), (1,0), (0,1), (0,-1)]:
                x1, y1 = curr_x + x, curr_y + y
                if -1 < x1 < r and -1 < y1 < c and (x1, y1) not in seen:
                    if grid[x1][y1]:
                        stack.append((x1, y1))
                        seen.add((x1, y1))
                        grid[x1][y1] = 'v'
        return area
    max_area = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i, j))
    return max_area 