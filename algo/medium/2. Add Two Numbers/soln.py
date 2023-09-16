def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time Complexity: O(max(l1, l2))
    Space Complexity: O(1)

    TODO:
    1. While both are not None, we add and check for carry
    2. Continue until both are None
    3. Return output linked list
    """
    output = ListNode()
    temp = output
    carry = 0
    while l1 or l2:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        add = (v1 + v2 + carry) % 10
        carry = (v1 + v2 + carry) // 10
        temp.next = ListNode(add)
        temp = temp.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    if carry:
        temp.next = ListNode(1)
    return output.next