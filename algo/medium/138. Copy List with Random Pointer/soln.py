class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    """
    Two Pass
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We add a new attribute to maintain the reference to the new copy node so that we can refer to it later to set it as the random. This is to ensure that we do not use extra space. We do this first to ensure that we can connect later on
    2. Second pass we can do the random connections
    3. We then return the head
    """
    sentinel = Node(0)
    dummy = sentinel
    temp = head

    while temp:
        node_copy = Node(temp.val)
        temp.new = node_copy # Store pointer for our new node to connect our randoms later

        dummy.next = node_copy
        dummy = dummy.next
        temp = temp.next

    while head:
        if head.random:
            head.new.random = head.random.new
        head = head.next

    return sentinel.next

    """
    Two Pass with Space
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Same as above but we store the old node as the dictionary instead of a class attribute
    2. We then iterate through it to store the new nodes. We then process it later in the second pass
    """
    node_map = {None: None}
    curr = head

    while curr:
        node_map[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        node_map[curr].next = node_map[curr.next]
        node_map[curr].random = node_map[curr.random]
        curr = curr.next
    return node_map[head]