# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        curr = head
        stack = []

        while curr:
            stack.append(curr)
            curr = curr.next
        
        L = len(stack)
        curr = head
        
        for _ in range(L//2):
            top = stack.pop()
            nxt = curr.next
            curr.next = top
            if nxt is top:
                top.next = None
                return
            top.next = nxt
            curr = nxt
        curr.next = None
