def inorderSuccessor(root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Append each node into array
    2. If prev is the desired node, we then return the node else None
    """
    output = []
    def traverse(head):
        if head:
            traverse(head.left)
            output.append(head)
            traverse(head.right)
    traverse(root)

    for i in range(1, len(output)):
        if output[i-1].val == p.val:
            return output[i]

    return None

    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    ---> Answer from editorial
    NOTE: Read up on BST properties again!!

    TODO:
    1. We use the properties of a BST
    2. If p.val is greater than current, we can just go to the right of node
    3. Else we iterate downwards and set successor as left side of node until None which gives us the successor
    """
    successor = None

    while root:
        if p.val >= root.val:
            root = root.right
        else:
            successor = root
            root = root.left
    return successor