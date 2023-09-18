def pathSum(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    """
    Time Complexity: O(n * 2) --> Copy our combination list
    Space Complexity: O(n) --> Call Stack

    TODO:
    1. Iterate through each node and get sum
    2. If remainder < 0, we append to output
    3. Else we stop looking
    4. Return the output
    """

    def dfs(total, combi, cache, root):
        if root and total + root.val == targetSum and not root.left and not root.right:
            cache.append(list(combi + [root.val]))
            return
        if not root:
            return

        dfs(total + root.val, combi + [root.val], cache, root.left)
        dfs(total + root.val, combi + [root.val], cache, root.right)

    output = []
    dfs(0, [], output, root)
    return output