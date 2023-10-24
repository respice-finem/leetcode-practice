from collections import deque

def largestValues(root: Optional[TreeNode]) -> List[int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We do a level order traversal
    2. In each level, we get check the max and switch the val if necessary
    3. Return the output
    """
    if not root:
        return []

    queue = deque()
    queue.append(root)
    output = []

    while queue:
        curr_len = len(queue)
        temp_max = float('-inf')
        for i in range(curr_len):
            curr_node = queue.popleft()
            temp_max = max(temp_max, curr_node.val)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        output.append(temp_max)
    return output