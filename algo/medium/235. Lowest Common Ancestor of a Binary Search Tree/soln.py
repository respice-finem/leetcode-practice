def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    Time Complexity: O(n)
    Space Complexity: O(n ^ 2)
    NOTE: Might be TLE since we check each nodes
    TODO:
    1. We do pre-order traversal while storing the ancestors in a dict
    2. We then check for respective nodes and iterate through their ancestors from behind to see if we can get the least common
    """
    ancestors = {}
    def preorder(root, curr_ancs = []):
        if root:
            new_ancs = curr_ancs + [root]
            ancestors[root.val] = new_ancs
            preorder(root.left, new_ancs)
            preorder(root.right, new_ancs)
    preorder(root, [root])
    for i in range(min(len(ancestors[p.val]), len(ancestors[q.val]))-1,-1,-1):
        if ancestors[p.val][i] == ancestors[q.val][i]:
            return ancestors[p.val][i]

    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    NOTE: Similar as above but we leverage property of BST
    TODO:
    1. We leverage on property of BST and search for key. We store ancestors for both p and q then do iteratively from behind to get common ancestor
    """
    def find_key(root, target):
        output = [root]
        if root.val == target.val:
            return output
        elif not root:
            return []
        elif root.val < target.val:
            val = find_key(root.right, target)
            return output + val
        else:
            val = find_key(root.left, target)
            return output + val
    ancs_p = find_key(root, p)
    ancs_q = find_key(root, q)
    for i in range(min(len(ancs_p), len(ancs_q))-1,-1,-1):
        if ancs_p[i] == ancs_q[i]:
            return ancs_p[i]

    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    NOTE: Optimal version
    --> We can just traverse accordingly
    TODO:
    1. All we need to check is if they fall under left and right or are equal to the values, otherwise we traverse based on its value
    """
    parent_val = root.val

    p_val = p.val
    q_val = q.val
    node = root

    while node:
        parent_val = node.val
        if p_val > parent_val and q_val > parent_val:
            node = node.right
        elif p_val < parent_val and q_val < parent_val:
            node = node.left
        else:
            return node