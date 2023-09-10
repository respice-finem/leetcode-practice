def spiralOrder(matrix: List[List[int]]) -> List[int]:
    """
    (Simulation style approach)
    Time Complexity: O(m*n) --> Size of matrix
    Space Complexity: O(1) --> Assuming the output we return is not the space we use
    else is O(n)
    
    TODO:
    1. Instantiate an empty array
    2. Start with left and continue moving until we hit the boundaries
    2.5 then we move down right and up
    3. Once we visited everything, return the list
    """
    output = []
    m_row, m_col = len(matrix), len(matrix[0])
    row, column = 0, -1

    while len(output) != m_row * m_col:
        while column + 1 <= m_col - 1 and matrix[row][column + 1] != 'v':
            column += 1
            output.append(matrix[row][column])
            matrix[row][column] = 'v'

        while row + 1 <= m_row - 1 and matrix[row + 1][column] != 'v':
            row += 1
            output.append(matrix[row][column])
            matrix[row][column] = 'v'

        while column - 1 >= 0 and matrix[row][column - 1] != 'v':
            column -= 1
            output.append(matrix[row][column])
            matrix[row][column] = 'v'

        while row - 1 >= 0 and matrix[row - 1][column] != 'v':
            row -= 1
            output.append(matrix[row][column])
            matrix[row][column] = 'v'

    return output

    """
    Same as above.
    Answer from editorial

    TODO:
    1. We follow the same approach as above but one main change is that instead of altering the matrix, we apply the same approach by constricting our boundaries
    """
    output = []
    right, down, up, left = len(matrix[0]) - 1, len(matrix) - 1, 0, 0

    while len(output) < len(matrix) * len(matrix[0]):
        # Rightwards
        for col in range(left, right + 1):
            output.append(matrix[up][col])
        
        # Downwards
        for row in range(up + 1, down + 1): # Up + 1 is to avoid duplicating the element that was visited in rightwards
            output.append(matrix[row][right])

        # Leftwards
        if up != down:
            for col in range(right - 1, left - 1, -1): # Right - 1 avoids duplicates in downwards
                output.append(matrix[down][col])

        # Upwards
        if left != right: # 
            for row in range(down - 1, up, -1): # Down - 1 avoids duplicates in leftwards
                output.append(matrix[row][left])
        
        right -= 1
        down -= 1
        up += 1
        left += 1

    return output