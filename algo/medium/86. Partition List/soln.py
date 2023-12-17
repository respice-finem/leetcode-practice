class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We create two list one for head, the other is for tail
    2. We then append accordingly to the condition
    3. We then join the two heads again
    """
    sentinel1 = ListNode()
    sentinel2 = ListNode()

    temp1 = sentinel1
    temp2 = sentinel2

    while head:
        if head.val < x:
            temp1.next = ListNode(head.val)
            temp1 = temp1.next
        else:
            temp2.next = ListNode(head.val)
            temp2 = temp2.next
        head = head.next
    temp1.next = sentinel2.next
    return sentinel1.next
    