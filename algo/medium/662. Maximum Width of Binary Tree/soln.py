from collections import deque
def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    NOTE: Minor optimization, we just have to use the earliest seen index vs the latest seen index, we do not need to count for each index

    TODO:
    1. Instead of iteratively building the levels, we just need to keep track the current index of the nodes
    """
    queue = deque()
    queue.append((root, 0))
    width = 0
    while queue:
        curr_len = len(queue)
        min_index = float('inf')
        max_index = float('-inf')
        for i in range(curr_len):
            curr_node, index = queue.popleft()
            min_index = min(min_index, index)
            max_index = max(max_index, index)
            if curr_node.left:
                queue.append((curr_node.left, index * 2))
            if curr_node.right:
                queue.append((curr_node.right, index * 2+1))
        width = max(width, max_index - min_index + 1)
    return width

    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Same as above but we optimize the calculations
    """
    queue = deque()
    queue.append((root, 0))
    width = 0
    while queue:
        curr_len = len(queue)
        _, head_index = queue[0]
        for i in range(curr_len):
            curr_node, index = queue.popleft()
            if curr_node.left:
                queue.append((curr_node.left, index * 2))
            if curr_node.right:
                queue.append((curr_node.right, index * 2+1))
        width = max(width, index - head_index + 1)
    return width

    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Same as above but we do it recursively with DFS
    """
    first_col_index_table = {}
    max_width = 0

    def DFS(node, depth, col_index):
        nonlocal max_width
        if node is None:
            return
        if depth not in first_col_index_table:
            first_col_index_table[depth] = col_index
        
        max_width = max(max_width, col_index - first_col_index_table[depth] + 1)

        DFS(node.left, depth + 1, 2 * col_index)
        DFS(node.right, depth + 1, 2 * col_index + 1)
    DFS(root, 0, 0)
    return max_width