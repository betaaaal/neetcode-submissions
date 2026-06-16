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
        if head==None:
            return None
        # create new list with same values
        curr= head
        while curr is not None:
            newNode= Node(curr.val)
            newNode.next=curr.next
            curr.next=newNode
            curr=newNode.next
        
        # copy all random pointers
        curr=head
        while curr is not None:
            if curr.random:
                curr.next.random=curr.random.next
            curr=curr.next.next
        
        # separate the two lists
        newHead=head.next
        curr=head
        newCurr=newHead
        while newCurr is not None:
            curr.next=newCurr.next
            curr=curr.next
            if curr:
                newCurr.next=curr.next
            newCurr=newCurr.next
        return newHead


