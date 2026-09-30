# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        if not head:
            return False
        index = 0
        while head is not None:
            if head in seen:
                return True
            index += 1
            seen[head] = 1
            head = head.next
        return False