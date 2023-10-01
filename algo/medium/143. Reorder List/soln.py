def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    """
    Two Pass
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We append our pointers into our array
    2. We then perform the connections from the array pointer
    """
    temp = head
    output = []
    while head:
        output.append(head)
        head = head.next
    left, right = 0, len(output) - 1

    while left < right:
        prev = output[left].next
        output[left].next = output[right]
        output[right].next = prev
        left += 1
        right -= 1
    output[left].next = None

    """
    Split and Reverse then Join
    Time Compelexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We first do a fast and slow to get the mid point
    2. We then reverse the second half of the linked list
    3. We then connect criss cross and return the head of the temp
    """

    # 1. Split and reverse
    output = head
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    while slow:
        temp = slow
        slow = slow.next
        temp.next = prev
        prev = temp

    # 2. Combine our reversed linked list and our current head
    # We have to deal with odd and even length splits
    while prev.next:
        temp1 = prev.next
        temp2 = head.next
        head.next = prev
        prev.next = temp2
        prev = temp1
        head = temp2

    """
    Cleaner Implementation
    --> Answer from editorial
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not head:
        return

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev, curr = None, slow
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    first, second = head, prev
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next