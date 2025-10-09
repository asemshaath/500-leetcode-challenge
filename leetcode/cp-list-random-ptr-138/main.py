"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return head
            
        curr = head

        while curr:
            nxt = curr.next
            curr.next = Node(curr.val, next=nxt)
            curr = curr.next.next
        
        curr = head

        while curr:
            # nxt = curr.next
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # delete every odd Node
        # 7 -> 7' -> 13 -> 13' -> 11 -> 11' ->:::
        
        # 7' -> 13'
        curr = head.next

        while curr and curr.next:
            curr.next = curr.next.next
            curr = curr.next
        return head.next
            
