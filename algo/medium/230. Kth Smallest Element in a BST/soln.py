def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Append all nodes then get kth-index root
    """
    nodes = []
    def traverse(root):
        if root:
            traverse(root.left)
            nodes.append(root.val)
            traverse(root.right)
    traverse(root)
    return nodes[k-1]

    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Same as above but iterative
    """
    stack = []

    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k:
            return root.val
        root = root.right