def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We have a even and odd pointer
    2. At each step, we have to check if we can still iterate i.e. if there are still next nodes
    3. If there are, we can do a double leap. Else we stop and combine the odd and evens
    4. We then return the head pointer which will yield us our new changes
    """
    if not head:
        return head

    temp = head.next
    even = head
    odd = head.next
    while even.next and odd.next:
        even.next = even.next.next
        odd.next = odd.next.next
        even = even.next
        odd = odd.next

    even.next = temp
    return head