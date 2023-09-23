from collections import deque

def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    """
    BFS

    Time Complexity: O(m * n)
    Space Complexity: O(m + n)

    TODO:
    1. We first get the indexes of the 0s
    2. We then get all the neighbors to be changed
    """
    r, c = len(matrix), len(matrix[0])
    queue = deque()
    seen = set()

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                queue.append((i,j))
                seen.add((i, j))

    while queue:
        x0, y0 = queue.popleft()
        
        for i in range(r):
            if (i, y0) not in seen:
                matrix[i][y0] = 0
                seen.add((i, y0))

        for i in range(c):
            if (x0, c) not in seen:
                matrix[x0][i] = 0
                seen.add((x0, i))
    
    """
    Sentinel Value (String)
    Time Complexity: O(m * n)
    Space Complexity: O(1)

    TODO:
    1. Instead creating an index of what we want to change to 0, we mark the starting row and column of interest to be None for those to be converted (Though some interviewers might not like the input matrix to be changed --> we keep this trick up our sleeves)
    2. We then run through the matrix again to convert those that are the special character to be 0
    """
    r, c = len(matrix), len(matrix[0])
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                for k in range(r):
                    if matrix[k][j] != 0 and matrix[k][j] != '#':
                        matrix[k][j] = '#'
                for k in range(c):
                    if matrix[i][k] != 0 and matrix[i][k] != '#':
                        matrix[i][k] = '#'

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == '#':
                matrix[i][j] = 0

    """
    Time Complexity: O(m * n)
    Space Complexity: O(1)
    --> Editorial answer (Very hard to think of this during interview)
    --> Just keep in mind that we can do this

    TODO:
    1. Key idea is to demarcate the top of the column with 0 and first of row to be 0. We then come back to fill them up.
    2. To handle not incorrectly filling up the matrices with 0s, we have to check if 0,0 is 0. If it is we would have to deal with it later. Otherwise we check if the first column contains 0, if it does then we have to set that whole column as 0. Otherwise we would use the first row and column to set our boundaries later
    """
    r, c = len(matrix), len(matrix[0])
    is_col = False

    for i in range(r):
        if matrix[i][0] == 0:
            is_col = True

        for j in range(1, c):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, r):
        for j in range(1, c):
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        for j in range(c):
            matrix[0][j] = 0

    if is_col:
        for i in range(r):
            matrix[i][0] = 0