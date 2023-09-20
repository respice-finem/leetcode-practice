from collections import deque

def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    """
    NOTE: TLE!!!!
    Suboptimal (Because we will be revisiting the same nodes again)
    Instead of starting from 1, we start from 0
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)

    TODO:
    1. We do a BFS for the 1s, we check if the other cells with 1s already have values, if they do we take those and return 1 + the current value of that cell
    2. For 0s, we just skip and enter 0s
    3. Return the copy matrix
    """
    r, c = len(mat), len(mat[0])
    output = [[0 for _ in range(c)] for _ in range(r)]

    # This revisits alot of visited nodes
    # NOTE: Also it doesn't store the values used, so we are wasting alot of computation
    def bfs(sr, sc):
        queue = deque()
        queue.append((sr, sc, output[sr][sc]))
        seen = set()
        while queue:
            x0, y0, dist = queue.popleft()
            for x, y in [(-1,0), (1,0), (0,1), (0,-1)]:
                x1, y1 = x + x0, y + y0
                if -1 < x1 < r and -1 < y1 < c and (x1, y1) not in seen:
                    if mat[x1][y1] == 1:
                        output[sr][sc] = 1 + dist
                        return
                    elif mat[x1][y1] == 1 and output[x1][y1] != 0:
                        output[sr][sc] = min(output[sr][sc], 1 + output[x1][y1])
                    if mat[x1][y1] == 1:
                        queue.append((x1, y1, dist+1))
                    seen.add((x1, y1))

    for i in range(r):
        for j in range(c):
            if mat[i][j] == 1:
                bfs(i, j)

    return output

    """
    Improvement from above
    ---> From editorial
    NOTE: We start from 0s, this reduces the overlap of our values
    IMPORTANT to note this, how do we prevent overlapping search spaces
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    r, c = len(mat), len(mat[0])
    output = [[0 for _ in range(c)] for _ in range(r)]
    queue = deque()
    seen = set()

    for i in range(r):
        for j in range(c):
            if mat[i][j] == 0:
                queue.append((i, j, 0))
                seen.add((i, j))

    while queue:
        x0, y0, steps = queue.popleft()
        for x, y in [(-1,0), (1,0), (0,1), (0,-1)]:
            x1, y1 = x + x0, y + y0
            if -1 < x1 < r and -1 < y1 < c and (x1, y1) not in seen:
                seen.add((x1, y1))
                queue.append((x1, y1, steps + 1))
                output[x1][y1] = steps + 1 # We do not need to worry about handling 0s since they will already be 0 in the first place

    return output

    """
    DP Approach (Memoization)
    --> Editorial Answer (Interesting way to look at the question)
    NOTE: Could be used in a different context that deals with generating shortest paths for nodes
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)

    TODO:
    1. Key idea is that each ones have a 1 + neighbor steps. Therefore, we have to calculate that via a two sweep approach. We break down our operations into two separate steps
    2. We first do an upper to bottom sweep to get the minimum only looking at the down and right components
    3. We then do a bottom to upper sweep to get the minimum only looking at the up and left components
    4. This allows us to get a full picture
    """
    r, c = len(mat), len(mat[0])
    output = [row[:] for row in mat]

    for row in range(r):
        for col in range(c):
            min_neighbor = float('inf')
            if output[row][col] != 0:
                if row > 0:
                    min_neighbor = min(min_neighbor, output[row -1][col])
                if col > 0:
                    min_neighbor = min(min_neighbor, output[row][col-1])
                output[row][col] = min_neighbor + 1

    for row in range(r-1,-1,-1):
        for col in range(c-1,-1,-1):
            min_neighbor = float('inf')
            if output[row][col] != 0:
                if row < r-1:
                    min_neighbor = min(min_neighbor, output[row+1][col])
                if col < c-1:
                    min_neighbor = min(min_neighbor, output[row][col+1])
                output[row][col] = min(output[row][col], min_neighbor + 1)
    return output