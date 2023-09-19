def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    """
    BFS Approach
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)

    TODO:
    1. We create a replicated matrix with empty vals
    2. We then do a BFS. Check if anything is around us that are neighbors with the same color as source
    3. If it is we keep it to be filled, else we discard it. We also keep the ones that we have seen.
    4. Once we have a list of all the indexes that we wanna fill and no more adjacents are available, we break and fill the image up
    5. Return the image
    """
    queue = deque()
    queue.append((sr, sc))
    seen = set([(sr, sc)])
    to_fill = set()

    if image[sr][sc] == color:
        return image
    else:
        to_fill.add((sr, sc))

    while queue:
        r, c = queue.popleft()
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r1, c1 = r + x, c + y
            if -1 < r1 < len(image) and -1 < c1 < len(image[0]) and (r1,c1) not in seen:
                if image[r1][c1] == image[sr][sc]:
                    queue.append((r1, c1))
                    to_fill.add((r1, c1))
                seen.add((r1, c1))
    for e in to_fill:
        image[e[0]][e[1]] = color
    return image

    """
    Cleaner Implentation for above

    Time Complexity: O(m * n)
    Space Complexity: O(1)

    TODO:
    1. Same as above without the other array
    """
    queue = deque()
    queue.append((sr, sc))
    seen = set((sr, sc))
    oldColor = image[sr][sc]
    image[sr][sc] = color

    if oldColor == color:
        return image

    while queue:
        r, c = queue.popleft()
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r1, c1 = r + x, c + y
            if -1 < r1 < len(image) and -1 < c1 < len(image[0]) and (r1,c1) not in seen:
                if image[r1][c1] == oldColor:
                    image[r1][c1] = color
                    queue.append((r1,c1))
                seen.add((r1,c1))
    return image

    """
    DFS Approach
    Time Complexity: O(m * n)
    Space Complexity: O(n) --> Call Stack

    TODO:
    1. Same as above but DFS
    2. Furthermore, we can not 
    """
    oldColor = image[sr][sc]
    if oldColor == color:
        return image

    def dfs(r, c):
        if image[r][c] == oldColor:
            image[r][c] = color
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r1, c1 = r + x, c + y
                if -1 < r1 < len(image) and -1 < c1 < len(image[0]):
                    dfs(r1, c1)

    dfs(sr, sc)
    return image