# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head

        while curr:
            size += 1
            curr = curr.next
        
        n_n = size - n + 1
        dummy = ListNode()
        curr = dummy
        i = 1

        while head:
            if i != n_n:
                curr.next = ListNode(val=head.val)
                curr = curr.next
            i += 1
            head = head.next
        
        return dummy.next
