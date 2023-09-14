def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    """
    Time Complexity: O(log (m*n))
    Space Complexity: O(1)

    TODO:
    1. We treat the 2D matrix as a 1D matrix (We convert the row and cols to an index form similar to a 1D)
    2. Perform binary search and check if target meets
    3. Return true if found else false
    """
    row, col = len(matrix), len(matrix[0])
    start = 0
    end = (row * col) - 1

    while start <= end:
        mid = (start + end) // 2
        r_mid, c_mid = mid // col, mid % col
        if matrix[r_mid][c_mid] == target:
            return True
        elif matrix[r_mid][c_mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return False