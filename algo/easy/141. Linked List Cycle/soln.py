def hasCycle(head: Optional[ListNode]) -> bool:
    """
    (Suboptimal)

    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We iterate through each node val
    2. Store the seen in a set or hashmap
    3. If the node appears more than once, we return True
    4. Else stop and return False
    """
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False
    
    """
    (Optimal)
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. Floyd's algorithm
    2. We set a slow and fast pointer
    3. Fast pointer moves twice as fast, slow moves one at a time
    4. If the fast pointer meets the slow, there is a cycle
    5. If the fast pointer reaches the end, we stop and return False
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False