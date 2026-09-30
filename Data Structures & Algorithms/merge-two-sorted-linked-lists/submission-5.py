# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        new_link = dummy
        while list1 is not None and list2 is not None:
            if list1.val >= list2.val:
                new_link.next = list2
                new_link = new_link.next
                list2 = list2.next
            else:
                new_link.next = list1
                new_link = new_link.next
                list1 = list1.next
        new_link.next = list1 or list2
        return dummy.next
