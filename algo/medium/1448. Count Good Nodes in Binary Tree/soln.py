def goodNodes(root: TreeNode) -> int:
    """
    Recursive DFS
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We start from the node then keep track of the running max
    2. If the current node is greater than the current max, we increment the good nodes. Else, we continue
    3. If we reach the end, we stop
    """
    def dfs(root, curr_max):
        outcome = 0
        if root:
            for node in (root.left, root.right):
                if node:
                    outcome += dfs(node, max(node.val, curr_max))
        return outcome +  1 * (root.val >= curr_max)

    return dfs(root, root.val)

    """
    BFS
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Same as above, but BFS approach
    """
    from collections import deque

    queue = deque()
    queue.append((root, float('-inf')))
    count = 0
    while queue:
        curr_node, curr_max = queue.popleft()
        if curr_max <= curr_node.val:
            count += 1
        for node in (curr_node.left, curr_node.right):
            if node:
                queue.append((node, max(curr_max, curr_node.val)))
    return count