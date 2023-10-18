from collections import deque

def wallsAndGates(rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We get all the walls/obstacles first and store the indexes
    2. We then perform BFS and only continue if the current distance is less than the distance that was found previously
    """
    r, c = len(rooms), len(rooms[0])
    queue = deque()

    for i in range(r):
        for j in range(c):
            if rooms[i][j] == 0:
                queue.append((i, j, 0))

    while queue:
        x0, y0, dist = queue.popleft()
        for x, y in [(-1,0), (1,0), (0,1), (0,-1)]:
            x1, y1 = x0 + x, y0 + y
            if -1 < x1 < r and -1 < y1 < c and rooms[x1][y1] not in (0, -1) and rooms[x1][y1] > dist + 1:
                queue.append((x1, y1, dist + 1))
                rooms[x1][y1] = dist + 1