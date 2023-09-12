def isPalindrome(head: Optional[ListNode]) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Iterate through the linked list and store the string
    2. Check if same as reverse
    """
    output = ""
    while head:
        output += str(head.val)
        head = head.next
    return output == output[::-1]

    """
    (Optimal)
    Time Complexity: O(n)
    Space Complexity: O(1) --> Constant space since pointers

    TODO:
    1. Split the linked list in half
    2. Reverse the second half of the linked list
    3. Iterate and check each node. Return false if different, else once ends are reached, return True
    """
    slow = fast = head

    # Split into half
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None

    # Reverse half
    while slow:
        temp = slow
        slow = slow.next
        temp.next = prev
        prev = temp

    # Compare half
    while prev and head:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next

    return not head or not head.next