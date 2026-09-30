# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        new_link = dummy
        head1 = list1
        head2 = list2
        while head1 is not None and head2 is not None:
            if head1.val >= head2.val:
                new_link.next = head2
                new_link = new_link.next
                head2 = head2.next
            else:
                new_link.next = head1
                new_link = new_link.next
                head1 = head1.next
        new_link.next = head1 or head2
        return dummy.next
