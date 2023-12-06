class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time Complexity: (nlogn)
    Space Complexity: O(log n) --> Call stack

    TODO:
    1. Similar approach to merge sort
    """
    def merge(left, right):
        sentinel = ListNode()
        temp = sentinel

        while left and right:
            if left.val <= right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next

        if left:
            temp.next = left
        if right:
            temp.next = right
        return sentinel.next

    def split(head):
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return head, slow

    def mergeSort(head):
        if not head or not head.next:
            return head

        left, right = split(head)
        newLeft = mergeSort(left)
        newRight = mergeSort(right)
        return merge(newLeft, newRight)

    return mergeSort(head)