def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    (Suboptimal)
    Slightly cleaner than editorial approach

    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We convert our linked list into an array
    2. Return the middle
    """
    output = []
    while head:
        output.append(head)
        head = head.next

    return output[len(output)//2] 

    """
    (Optimal)
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We set two pointers, fast and slow
    2. Fast will traverse twice as fast as slow (moves one at a time)
    3. When fast reaches the end, we return the slow since it would be in the middle
    """
    slow = fast = head
    # We check if next node is None or current is already None
    # End has been reached
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow