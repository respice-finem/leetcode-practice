def isValidBST(root: Optional[TreeNode]) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We do a in-order traversal
    2. The values should be strictly increaing
    3. If not return False, else True
    """
    check = []
    def traverse(root):
        if root:
            traverse(root.left)
            check.append(root.val)
            traverse(root.right)
    traverse(root)
    for i in range(1, len(check)):
        if check[i-1] >= check[i]:
            return False
    
    return True

    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    --> Answer from editorial
    NOTE: If we can't use self, would be better for us to use the iterative approach below
    TODO:
    1. Same as above but instead of keeping an array, we just need to keep a previous val
    """
    def inorder(root):
        if not root:
            return True
        if not inorder(root.left):
            return False
        if root.val <= self.prev:
            return False
        self.prev = root.val
        return inorder(root.right)
    self.prev = -math.inf
    return inorder(root)

    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Same as above but we do it iteratively
    """
    stack, prev = [], -math.inf

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val <= prev:
            return False
        prev = root.val
        root = root.right
    return True