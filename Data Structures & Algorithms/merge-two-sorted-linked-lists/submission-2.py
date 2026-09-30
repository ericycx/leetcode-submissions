# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        head1 = list1
        head2 = list2
        if list1.val >= list2.val:
            first = list2
            new_link = list2
            head2 = first.next
        else:
            first = list1
            new_link = list1
            head1 = first.next
        while head1 is not None and head2 is not None:
            if head1.val >= head2.val:
                new_link.next = head2
                new_link = new_link.next
                head2 = head2.next
            else:
                new_link.next = head1
                new_link = new_link.next
                head1 = head1.next
        if head1 is None:
            new_link.next = head2
        else:
            new_link.next = head1
        return first
