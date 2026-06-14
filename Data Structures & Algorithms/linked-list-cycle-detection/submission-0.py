# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=head
        l=[]
        while temp is not None:
            if temp not in l:
                l.append(temp)
            else:
                return True
            temp=temp.next
        else:
            return False
