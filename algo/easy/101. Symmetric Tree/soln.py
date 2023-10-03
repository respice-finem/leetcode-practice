def isSymmetric(root: Optional[TreeNode]) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n) --> Call Stack

    TODO:
    1. We check left vs right is the same
    2. We then check right vs left is the same
    3. Return the final output
    """
    def equal(a, b):
        if not a and not b:
            return True
        if (not a and b) or (a and not b):
            return False
        if a.val != b.val:
            return False
        else:
            return True and equal(a.left, b.right) and equal(a.right, b.left)
            
    return equal(root.left, root.right)

    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Same as above but we do it iterative
    """
    from collections import deque

    queue = deque()
    queue.append(root.left)
    queue.append(root.right)

    while queue:
        n1 = queue.popleft()
        n2 = queue.popleft()
        if not n1 and not n2:
            continue
        if not n1 or not n2:
            return False
        if n1.val != n2.val:
            return False
        queue.append(n1.left)
        queue.append(n2.right)
        queue.append(n1.right)
        queue.append(n2.left)
    return True