# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time Complexity: O(m + n)
    Space Complexity: O(m + n)

    TODO:
    1. We put the elements into two stacks by iterating through them
    2. We then pop and check if we need to carry and generate the new nodes and append accordingly
    3. Once we reach the end, we check if there is carry, if there is we then add 1 in the front
    4. Else we just return the next node
    """
    stack1 = []
    stack2 = []

    while l1:
        stack1.append(l1.val)
        l1 = l1.next

    while l2:
        stack2.append(l2.val)
        l2 = l2.next

    carry = 0
    next_node = None
    while stack1 or stack2:
        val1 = stack1.pop() if stack1 else 0
        val2 = stack2.pop() if stack2 else 0
        add = val1 + val2 + carry
        carry = int(add / 10)
        add %= 10
        curr = ListNode(add, next=next_node)
        next_node = curr
    if carry:
        return ListNode(carry, next_node)
    return next_node

    """
    Time Complexity: O(m + n)
    Space Complexity: O(1)

    TODO:
    1. We reverse both of the strings which give us a similar output as add two numbers I
    2. We then iterate through both and continue adding until we reach the end. Check if we need to deal with carry at the end
    3. Return the head
    """
    def reverse(head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev 
            prev = curr
        return prev
    l1_rev = reverse(l1)
    l2_rev = reverse(l2)
    
    carry = 0
    next_node = None
    while l1_rev or l2_rev:
        val1 = l1_rev.val if l1_rev else 0
        val2 = l2_rev.val if l2_rev else 0
        add = val1 + val2 + carry
        carry = int(add / 10)
        add %= 10
        curr = ListNode(add, next_node)
        next_node = curr
        if l1_rev:
            l1_rev = l1_rev.next
        if l2_rev:
                l2_rev = l2_rev.next
        if carry:
            return ListNode(1, next_node)
        return next_node