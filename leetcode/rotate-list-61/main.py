# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k == 0:
            return head
        if not head or not head.next:
            return head

        L = self.get_ll_size(head)
        k = k % L
        h1 = L - k

        curr = head
        while curr and curr.next and h1 > 1:
            h1 -= 1
            curr = curr.next
        
        new_head = curr.next
        new_tail = curr
        curr.next = None
        curr = new_head

        while curr and curr.next:
            curr = curr.next

        if curr:
            curr.next = head
            head = new_head
            return new_head

        return head

    def get_ll_size(self, head):
        size = 0
        curr = head

        while curr:
            size += 1
            curr = curr.next
        
        return size
            
