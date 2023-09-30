def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We instantiate a stack and an output array. We also keep a forward flag to indicate how we want to traverse the tree
    2. While we have nodes in our stack, we basically sweep according to the forward flag. if forward, we sweep L->R, if not forward we sweep R->L
    3. We then append the vals and return the output
    """
    if not root:
        return []

    forward = -1
    stack = [root]
    output = []
    while stack:
        temp = []
        output.append([e.val for e in stack])
        for i in range(len(stack)-1, -1, -1):
            val = stack[i]
            if forward > 0:
                if val.left:
                    temp.append(val.left)
                if val.right:
                    temp.append(val.right)
            elif forward < 0:
                if val.right:
                    temp.append(val.right)
                if val.left:
                    temp.append(val.left)
        stack = temp
        forward *= -1
    return output

    """
    (BFS Approach)
    Time Complexity: O(n)
    Space Complexity: O(n)
    --> Answer from editorial

    TODO:
    1. Similar to above, difference is for each level we add a None to signal change in direction like our flag
    2. The sweep is dependent to the is_order_left
    """
    ret = []
    level_list = deque()
    if root is None:
        return []
    node_queue = deque([root, None])
    is_order_left = True

    while len(node_queue) > 0:
        curr_node = node_queue.popleft()

        if curr_node:
            if is_order_left:
                level_list.append(curr_node.val)
            else:
                level_list.appendleft(curr_node.val)
            if curr_node.left:
                node_queue.append(curr_node.left)
            if curr_node.right:
                node_queue.append(curr_node.right)
        else:
            ret.append(level_list)
            if len(node_queue) > 0:
                node_queue.append(None)

            level_list = deque()
            is_order_left = not is_order_left
    return ret