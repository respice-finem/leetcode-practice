def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. Get length of the linked list
    2. Determine where to rotate
    3. Perform rotation
    """
    if not head or not head.next:
        return head
    
    # 1. Get length
    length = 0
    temp = head
    while temp:
        length += 1
        temp = temp.next

    # 2. Get Index
    to_rotate = (length - k) % length
    if to_rotate == 0:
        return head

    # 3. Perform rotation
    prev, curr = None, head
    for i in range(to_rotate):
        prev = curr
        curr = curr.next

    if prev:
        prev.next = None
    temp = curr
    while temp.next:
        temp = temp.next
    temp.next = head
    return curr
    
    """
    Cleaner Implementation
    --> Answer from editorial
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Same as above but we don't break and connect again
    """
    if not head or not head.next:
        return head

    old_tail = head
    n = 1
    while old_tail.next:
        old_tail = old_tail.next
        n += 1
    old_tail.next = head

    new_tail = head
    for i in range(n - k%n - 1):
        new_tail = new_tail.next
    new_head = new_tail.next

    new_tail.next = None
    return new_head