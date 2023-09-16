def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    One Pass

    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We setup a dummy node to act as previous. Connect to the current head
    2. We append all the previous and current nodes to a list
    3. Once we reach the end of the linked list, we choose the index and perform our change
    4. Return the dummy.next as output
    """
    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy

    pointer_arr = []
    while head:
        pointer_arr.append((prev, head))
        prev = head
        head = head.next

    to_remove = len(pointer_arr) - n
    e = pointer_arr[to_remove]
    e[0].next = e[1].next

    return dummy.next

    """
    One Pass solution with constant space

    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. Similar to above, but we do not store the values
    2. Instead, we will maintain a distance between the two pointers based on n
    3. Once we reach the end for the faster pointer, we remove the slow pointer and combine the prev and next
    4. We then return the dummy.next as output
    """
    dummy = ListNode(-1)
    dummy.next = head

    prev = dummy
    slow = fast = head

    while n:
        fast = fast.next
        n -= 1

    while fast:
        prev = slow
        slow = slow.next
        fast = fast.next
    prev.next = slow.next
    return dummy.next