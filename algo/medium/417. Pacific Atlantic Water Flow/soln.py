def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    """
    BFS
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)

    TODO:
    1. We create an empty matrix first and start from the Pacific Ocean, indicating the matrix with  reachable areas 
    2. We then start from the Atlantic Ocean indicating the matrix with reachable areas
    3. For those that overlap, we return the index
    """
    r, c = len(heights), len(heights[0])
    matrix = [[0 for _ in range(c)] for _ in range(r)]

    # BFS from Pacific Ocean
    pacific_start = set([(i, 0) for i in range(r)] + [(0, i) for i in range(c)])
    for x,y in pacific_start:
        matrix[x][y] = 1
    queue = deque(pacific_start)
    seen = pacific_start
    
    while queue:
        x0, y0 = queue.popleft()
        for x, y in [(-1,0), (1,0), (0,1), (0,-1)]:
            x1, y1 = x0 + x, y0 + y
            if -1 < x1 < r and -1 < y1 < c and (x1, y1) not in seen:
                if heights[x1][y1] >= heights[x0][y0]:
                    matrix[x1][y1] = 1
                    queue.append((x1, y1))
                    seen.add((x1, y1))

    # BFS from Atlantic Ocean
    atlantic_start = set([(i, c-1) for i in range(r)] + [(r-1, i) for i in range(c)])
    for x,y in atlantic_start:
        if matrix[x][y] == 1:
            matrix[x][y] += 1
        else:
            matrix[x][y] = 1
    queue = deque(atlantic_start)
    seen = atlantic_start

    while queue:
        x0, y0 = queue.popleft()
        for x, y in [(-1,0), (1,0), (0,1), (0,-1)]:
            x1, y1 = x0 + x, y0 + y
            if -1 < x1 < r and -1 < y1 < c and (x1, y1) not in seen:
                if heights[x1][y1] >= heights[x0][y0]:
                    if matrix[x1][y1] == 1:
                        matrix[x1][y1] += 1
                    else:
                        matrix[x1][y1] = 1
                    queue.append((x1, y1))
                    seen.add((x1, y1))
    
    output = []
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 2:
                output.append([i,j])
    return output

    """
    DFS
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)

    TODO:
    1. Same as above but we do a DFS instead
    """
    if not heights or not heights[0]:
        return []

    num_rows, num_cols = len(heights), len(heights[0])
    pacific_reachable = set()
    atlantic_reachable = set()

    def dfs(row, col, reachable):
        reachable.add((row, col))
        for x, y in [(-1,0), (1,0), (0,1), (0,-1)]:
            new_row, new_col = row + x, col + y
            if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                continue
            if (new_row, new_col) in reachable:
                continue
            if heights[new_row][new_col] < heights[row][col]:
                continue
            dfs(new_row, new_col, reachable)
    
    for i in range(num_rows):
        dfs(i, 0, pacific_reachable)
        dfs(i, num_cols-1, atlantic_reachable)
    for i in range(num_cols):
        dfs(0, i, pacific_reachable)
        dfs(num_rows-1,i, atlantic_reachable)

    return list(pacific_reachable.intersection(atlantic_reachable))