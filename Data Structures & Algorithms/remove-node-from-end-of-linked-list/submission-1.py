# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = first2 = end = head
        count = 0
        while end:
            count += 1
            end = end.next
        
        index = count - n - 1
        
        while index > 0:
            first2 = first2.next
            index -= 1
        
        if index < 0:
            return first.next
        
        if first2.next:
            first2.next = first2.next.next
        else:
            return None


        return first