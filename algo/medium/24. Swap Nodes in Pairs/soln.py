def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    (Iterative Approach)
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We connect a dummy node to the head
    2. Starting from the dummy node, we then have to perform a 3 step cycle which is as follows:
    a) In each cycle: It will smth like this (N) --> (L) --> (R) --> (Another Val)
    where N is the pivot. L is Left side of swap and R is right side of swap
    b) We start by Connnecting the pivot to the right side of swap
    c) We then connect the left to the next val
    d) Finally we connect the right to the left to complete the swap
    e) We repeat this when we have a valid swap candidate
    3. One step 2 completes, we just get everyth after the dummy node
    """
    if not head or not head.next:
        return head
    dummy = ListNode(-1)
    dummy.next = head
    temp = dummy

    while temp.next and temp.next.next:
        left = temp.next
        right = temp.next.next

        temp.next = right
        left.next = right.next
        right.next = left

        temp = left
    return dummy.next

    """
    (Recursive Approach)
    --> From editorial, look into this again
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We perform the same method as the recursive
    """ 
    if not head or not head.next:
        return head

    first_node = head
    second_node = head.next

    first_node.next = self.swapPairs(second_node.next)
    second_node.next = first_node

    return second_node 