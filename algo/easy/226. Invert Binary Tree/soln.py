def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Time Complexity: O(n) --> Go through every single node
    Space Complexity: O(1) --> Reusing same tree

    TODO:
    1. Start from root
    2. Recursively go down and switch the nodes
    3. Until none, stop operation
    """
    if root:
        root.left, root.right = root.right, root.left # Make use of Python swap syntax
        invertTree(root.left)
        invertTree(root.right)
    return root  # Initial call stack will return the root of the tree

    """
    Cleaner Implementation

    Time Complexity: O(n) --> Go through every single node
    Space Complexity: O(1) --> Reusing same tree

    TODO:
    1. Start from root
    2. Recursively go down and switch the nodes
    3. Until none, stop operation
    """
    if not root:
        return root
    root.left, root.right = root.right, root.left
    for node in [root.left, root.right]:
        if node: # Remove unnecessary call stacks (Slight improvement)
            invertTree(node)
    return root # Initial call stack will return the root of the tree