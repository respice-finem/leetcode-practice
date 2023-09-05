def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    (Iterative Approach)
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. Setup variables to hold our prev and temp
    2. Iterate through the list and move our temp to hold the curr val
    2.5 Move the curr to the next
    3. Flip the next to the prev
    3.5 Set the temp to prev
    4. Repeat till we reach the end
    5. We return the new head which is our temp since it is the new head
    """
    prev = None

    while head:
        temp = head
        head = head.next
        temp.next = prev
        prev = temp
    return prev

    """
    (Recursive Approach)
    (As per editorial answer: https://leetcode.com/problems/reverse-linked-list/editorial/)

    Time Complexity: O(n)
    Space Complexity: O(n) --> Call Stack

    TODO:
    Same as iterative but some slight tweaks
    """
    if (not head) or (not head.next):
        return head
    
    p = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return p