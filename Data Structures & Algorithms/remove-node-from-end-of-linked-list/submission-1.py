# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length=0
        while curr is not None:
            length+=1
            curr=curr.next
        m=length-n
        if m==0:
            return head.next
        count=1
        curr=head
        while count<m:
            curr=curr.next
            count+=1
        front=curr.next
        curr.next=front.next
        return head
