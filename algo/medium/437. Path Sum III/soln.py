def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
    """
    (DFS) --> Suboptimal
    Time Complexity: O(n^2)
    Space Complexity: O(h)
    NOTE: Inefficient as we would be wasting computations while performing DFS
    TODO:
    1. We go through each nodes and perform a DFS and keep track of the value
    """
    def runningSum(root, total):
        nonlocal paths
        if total == targetSum:
            paths += 1
        if not root.left and not root.right:
            return
        for node in (root.left, root.right):
            if node:
                runningSum(node, total + node.val)
            
    if not root:
        return 0

    queue = deque()
    queue.append(root)
    paths = 0
    while queue:
        curr_node = queue.popleft()
        runningSum(curr_node, curr_node.val)
        for node in (curr_node.left, curr_node.right):
            if node:
                queue.append(node)
    return paths

    """
    (Prefix Sum)
    Time Complexity: O(n)
    Space Complexity: O(n)
    --> Answer from Editorial
    NOTE: As brainstormed, we need to maintain a prefix sum. The difficulty is maintaining the items of our calculations
    TODO:
    1. We keep a running count separate from our call stack and then we do preorder traversal across all the nodes. This ensures that it visits the node from up to bottom
    2. We then check for two things: if sum is equivalent to target vals we add to count, else we check if previous sums have the value, we then add
    3. Once we move back up we reduce the sum to prevent it from being use again
    """
    def preorder(root, total):
        nonlocal count
        if not root:
            return
        total += root.val
        if total == targetSum:
            count += 1

        count += sum_dict[total-targetSum]

        sum_dict[total] += 1
        preorder(root.left, total)
        preorder(root.right, total)

        sum_dict[total] -= 1 # How we perform the removal is here

    count = 0
    sum_dict = defaultdict(int)
    preorder(root, 0)
    return count