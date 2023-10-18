def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We run a DFS. Once we reach the end, we then propagate the value upwards to be True
    """
    if not root:
        return False

    def dfs(root, total):
        if not root.right and not root.left and total == targetSum:
            return True
        elif not root.right and not root.left and total != targetSum:
            return False
        outcome = False
        for node in (root.left, root.right):
            if node:
                outcome = dfs(node, total + node.val)
                if outcome:
                    return True
        return outcome

    return dfs(root, root.val)

    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Instead of DFS, we just do BFS
    """
    if not root:
        return False
    queue = deque()
    queue.append((root, root.val))

    while queue:
        curr_node, total = queue.popleft()
        if not curr_node.right and not curr_node.left and total == targetSum:
            return True
        for node in (curr_node.left, curr_node.right):
            if node:
                queue.append((node, total+node.val))
    return False