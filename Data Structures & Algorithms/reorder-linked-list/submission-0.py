# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        length=0
        while curr is not None:
            length+=1
            curr=curr.next
        mid=(length+1)//2
        count=1
        curr=head
        while count<mid:
            curr=curr.next
            count+=1
        # Split the list into two halves
        head1 = curr.next
        curr.next = None
        # reverse second half
        prev=None
        while head1 is not None:
            front=head1.next
            head1.next=prev
            prev=head1
            head1=front
        head2=prev #reversed second half
        head3=head #front half first 
        while head2:
            next1=head3.next
            next2=head2.next
            head3.next=head2
            head2.next=next1
            head3=next1
            head2=next2
        return 
        


        
