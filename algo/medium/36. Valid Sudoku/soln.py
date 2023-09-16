def isValidSudoku(board: List[List[str]]) -> bool:
    """
    Three Pass
    ---> This is the most intuitive
    Time Complexity: O(1) --> Since it is fixed as a 9*9 board
    Space Complexity: O(1)

    TODO:
    1. Follow the rules as stated in the question nothing special
    """
    # Row Checks
    def row_check(matrix):
        for i in range(9):
            seen = set()
            for j in range(9):
                if matrix[i][j] not in seen and matrix[i][j] != ".":
                    seen.add(matrix[i][j])
                elif matrix[i][j] in seen:
                    return False
        return True

    # Column Checks
    def column_check(matrix):
        for i in range(9):
            seen = set()
            for j in range(9):
                if matrix[j][i] not in seen and matrix[j][i] != ".":
                    seen.add(matrix[j][i])
                elif matrix[j][i] in seen:
                    return False
        return True

    # Grid check
    def grid_check(matrix):
        def single_grid(matrix, r, c):
            seen = set()
            for i in range(r, r+3):
                for j in range(c, c + 3):
                    if matrix[i][j] not in seen and matrix[i][j] != ".":
                        seen.add(matrix[i][j])
                    elif matrix[i][j] in seen:
                        return False
            return True
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not single_grid(matrix, i, j):
                    return False
        return True
    return row_check(board) and column_check(board) and grid_check(board)

    """
    Single Pass
    Time Complexity: O(1)
    Space Complexity: O(1)

    TODO:
    1. We can do a one pass check
    2. Something to note is that box we have to adjust accordingly
    """
    N = 9
    rows = [[0] * N for _ in range (N)]
    cols = [[0] * N for _ in range (N)]
    boxes = [[0] * N for _ in range (N)]

    for r in range(N):
        for c in range(N):
            if board[r][c] == '.':
                continue

            pos = int(board[r][c]) - 1

            if rows[r][pos] == 1:
                return False
            rows[r][pos] = 1

            if cols[c][pos] == 1:
                return False
            cols[c][pos] = 1

            idx = (r//3) * 3 + c // 3
            if boxes[idx][pos] == 1:
                return False
            boxes[idx][pos] = 1
    
    return True