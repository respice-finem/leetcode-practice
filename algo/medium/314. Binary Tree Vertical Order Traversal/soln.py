from collections import deque

def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We do a level order traversal. We then do for each col we -1 for left and + 1 for right. We then allocate empty arrays for left, mid and right.
    2. For negative we append left. If 0 we append mid. If more than 0 we append left
    3. We then add everything when we get the vals
    """
    if not root:
        return []
    left, mid, right = [], [[]], []
    queue = deque([(root, 0)])

    while queue:
        curr_length = len(queue)
        for i in range(curr_length):
            e, index = queue.popleft()
            if index > 0:
                if index > len(right):
                    right.append([e.val])
                else:
                    right[index-1].append(e.val)
            elif index < 0:
                if abs(index) > len(left):
                    left = [[e.val]] + left
                else:
                    left[index].append(e.val)
            else:
                mid[index].append(e.val)
            if e.left:
                queue.append((e.left, index-1))
            if e.right:
                queue.append((e.right, index+1))

    return left + mid + right

    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. Slightly optimized approach, we do not have to check the vals. Instead we keep track of the min column and max column and iterate to get the vals later
    """
    if not root:
        return []

    output = {}
    min_col = float('inf')
    max_col = float('-inf')
    queue = deque([(root, 0)])

    while queue:
        node, index = queue.popleft()
        min_col = min(index, min_col)
        max_col = max(index, max_col)
        if index not in output:
            output[index] = [node.val]
        else:
            output[index].append(node.val)
        if node.left:
            queue.append((node.left, index-1))
        if node.right:
            queue.append((node.right, index+1))
    return [output[i] for i in range(min_col, max_col+1)]

            