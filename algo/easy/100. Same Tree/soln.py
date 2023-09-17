from collections import deque

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        (Recursive Approach)
        Time Complexity: O(n)
        Space Complexity: O(n) --> Call Stack

        TODO:
        1. We go the same direction and check the vals
        2. If they are different we return False, else if we reach the end for both we return True
        """
        val1 = p.val if p else None
        val2 = q.val if q else None

        if val1 != val2:
            return False
        elif not p and not q:
            return True
        else:
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        """
        Iterative Approach
        Time Complexity: O(n)
        Space Complexity: O(n)

        TODO:
        1. We perform BFS and do our checks
        2. If we meet anything that is not same we return False
        """
        queue = deque([(p, q)])
        while queue:
            p, q = queue.popleft()
            if not p and not q:
                continue
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))

        return True