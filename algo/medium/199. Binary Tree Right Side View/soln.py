def rightSideView(root: Optional[TreeNode]) -> List[int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We can just do a BFS and get the right most node
    2. We get the values and append to output
    3. Return output
    """
    if not root:
        return []

    stack = [root]
    output = []

    while stack:
        temp = []
        output.append(stack[-1].val)
        for e in stack:
            if e.left:
                temp.append(e.left)
            if e.right:
                temp.append(e.right)
        stack = temp
    return output

    """
    (One Queue)
    Time Complexity: O(n)
    Space Complexity: O(n)
    ---> Answer from editorial

    TODO:
    1. By levels, we check the length and get the end of previous queue to get the previous right.
    2. We continue to iterate to append the nodes until we reach None
    """
    from collections import deque

    if not root:
        return []

    queue = deque([root, ])
    rightside = []

    while queue:
        level_length = len(queue)

        for i in range(level_length):
            node = queue.popleft()
            
            if i == level_length - 1:
                rightside.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return rightside