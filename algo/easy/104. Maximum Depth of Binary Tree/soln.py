def maxDepth(root: Optional[TreeNode]) -> int:
    """
    BFS

    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We iterate through each layer and get the current level
    2. We then compare the max depth at each level
    """
    from collections import deque

    if not root:
        return 0

    queue = deque()
    queue.append((root, 1))
    max_depth = 1

    while queue:
        node, level = queue.popleft()
        max_depth = max(max_depth, level)
        for new_node in (node.right, node.left):
            if new_node:
                queue.append((new_node, level + 1))
    return max_depth

    """
    DFS

    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We go to the deepest and compare the max at each point
    """
    if not root:
        return 0
    else:
        left = maxDepth(root.left)
        right = maxDepth(root.right)
        return max(left, right) + 1