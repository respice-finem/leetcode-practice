from collections import deque

def getFood(grid: List[List[str]]) -> int:
    """
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    --> For shortest path usually BFS is better

    TODO:
    1. We do a BFS. We check all neighbors and keep count of the number steps taken
    2. We take not
    3. If we run out of options we return -1.
    """
    r,c = len(grid), len(grid[0])
    queue = deque()
    seen = set()

    # Find starting point
    for i in range(r):
        for j in range(c):
            if grid[i][j] == "*":
                queue.append((i, j, 0))
                seen.add((i, j))
                break

    while queue:
        x0, y0, steps = queue.popleft()
        for x, y in [(-1,0), (1,0), (0, -1), (0,1)]:
            temp_x1, temp_y1 = x0 + x, y0 + y
            if -1 < temp_x1 < r and -1 < temp_y1 < c and (temp_x1, temp_y1) not in seen:
                if grid[temp_x1][temp_y1] == "O":
                    queue.append((temp_x1, temp_y1, steps + 1))
                elif grid[temp_x1][temp_y1] == "#":
                    return steps + 1
                seen.add((temp_x1, temp_y1))

    return -1