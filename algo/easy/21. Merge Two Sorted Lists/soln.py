# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        """
        Time Complexity: O(m+n)
        Space Complexity: O(m+n)

        TODO:
        1. Create empty pointer
        2. Compare the two node values while list1/2 are not None
        3. Take the smaller one and connect the head and go next
        4. If we finish iterating, we then fit the list to output node list
        """
        head = ListNode()
        temp = head
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            elif list2.val < list1.val:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        if list1:
            temp.next = list1
        if list2:
            temp.next = list2

        return head.next