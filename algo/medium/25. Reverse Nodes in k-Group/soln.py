class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We should keep track of the first and last element so then we reach the last element, we will perform any necessary reconnection of the linked list.
    2. Reattach the new head to the prev head and the new tail to the head.next
    """
    sentinel = ListNode()

    def reverse(start):
        reversePrev = None
        while start:
            curr = start
            start = start.next
            curr.next = reversePrev
            reversePrev = curr
        return reversePrev # Return new head

    # NOTE: We might have to consider edge case of k = 1, which is regular reversal
    temp = head
    counter = 0
    prev = sentinel
    while temp:
        counter += 1
        if counter == 1:
            start = temp
        if counter == k:
            next_node = temp.next
            temp.next = None
            new_start = reverse(start)
            prev.next = new_start
            start.next = next_node
            temp = start
            prev = start
            counter = 0
        
        temp = temp.next
    return sentinel.next