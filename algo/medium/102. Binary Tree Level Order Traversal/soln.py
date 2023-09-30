def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We basically do a BFS and append the results each level to the output
    """
    if not root:
        return []

    stack = [root]
    output = []

    while stack:
        temp = []
        output.append([e.val for e in stack])
        for e in stack:
            if e.left:
                temp.append(e.left)
            if e.right:
                temp.append(e.right)
        
        stack = temp
    
    return output

    """
    Level Based Implementation

    Time Complexity: O(n)
    Space Complexity: O(n)
    --> Answer from editorial

    TODO:
    1. Instead of creating a new array as above, we place the levels inside the output and append into it directly.
    """
    from collections import deque

    levels = []
    if not root:
        return levels

    level = 0
    queue = deque([root,])

    while queue:
        levels.append([])
        level_length = len(queue)

        for i in range(level_length):
            node = queue.popleft()
            levels[level].append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        level += 1

    return levels