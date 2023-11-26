class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head: 'Optional[Node]') -> 'Optional[Node]':
    """
    Time Complexity: O(n)
    Space Complexity: O(n) --> Call stack

    TODO:
    1. We do it recursively, if it's a child we set as next and relink the nodes. Set child as null then we continue iterating through the child while maintaining the previous next to be linked later
    2. We stop when we meet the end and we 
    """
    def traverse(root):
        while root:
            if root and not root.child and not root.next:
                return root
            if root.child:
                next_node = root.next
                root.next = root.child
                root.child = None
                root.next.prev = root
                root = root.next
                curr_node = traverse(root)
                curr_node.next = next_node
                if next_node:
                    next_node.prev = curr_node
                    root = next_node
                else:
                    root = curr_node
            else:
                root = root.next
    traverse(head)
    return head
                
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We do an iterative approach. We do the same as above. But more elegantly
    """
    if not head:
        return

    sentinel = Node(0, None, head, None)
    prev = sentinel

    stack = []
    stack.append(head)

    while stack:
        curr = stack.pop()

        prev.next = curr
        curr.prev = prev

        if curr.next:
            stack.append(curr.next)
        if curr.child:
            stack.append(curr.child)
            curr.child = None
        prev = curr

    sentinel.next.prev = None
    return sentinel.next