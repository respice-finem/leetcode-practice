from collections import deque
from functools import lru_cache

def minKnightMoves(x: int, y: int) -> int:
    """
    BFS with pruning
    Time Complexity: O((max(|x|, |y|))^2)
    Space Compleixty: O((max(|x|, |y|))^2)

    TODO:
    1. We can effectively limit our search space to only Quadrant 1. This is becasue all steps would be the same in any of the 4 quadrants since they are reflections of each other from the origin, as such we reduce the search space.
    2. We can do this by taking the absolute value of the x, y. We then perform BFS on the space and return the number of steps taken
    """
    abs_x, abs_y = abs(x), abs(y)
    if (abs_x, abs_y) == (0, 0):
        return 0

    queue = deque()
    queue.append((0, 0, 0))
    seen = set()
    seen.add((0, 0))

    while queue:
        x0, y0, steps = queue.popleft()
        for x, y in [(-2, -1), (-2,1), (2,-1), (2,1), (-1,2), (1,2), (-1,-2), (-1,2)]:
            x1, y1 = x + x0, y + y0
            if (x1, y1) not in seen:
                if (x1, y1) == (abs_x, abs_y):
                    return 1 + steps
                queue.append((x1,y1,1+steps))
                seen.add((x1,y1))

    """
    DFS Approach (Optimal)
    --> Answer from Editorial
    --> Leverages on the symmetry of the points on a grid
    --> NOTE: Take some time to read the solution to this 

    TODO:
    1. We start from the endpoint and see if it gets to (0,0) or any point that is close to an immediate neighbor which is two steps away
    2. We then return the minimum of the zigzag
    """
    @lru_cache(maxsize=None)
    def dfs(x, y):
        if x + y == 0:
            return 0
        elif x + y == 2:
            return 2
        else:
            return min(dfs(abs(x-1), abs(y-2)), dfs(abs(x-2), abs(y-1))) + 1
    return dfs(abs(x), abs(y))