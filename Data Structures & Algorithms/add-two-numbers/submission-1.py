# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        len1=0
        num1=0
        while curr is not None:
            len1+=1
            num1+=curr.val*(10**(len1-1))
            curr=curr.next
        curr = l2
        len2=0
        num2=0
        while curr is not None:
            len2+=1
            num2+=curr.val*(10**(len2-1))
            curr=curr.next
        num3=num1+num2
        l3=ListNode(0)
        if num3==0:
            return l3
        curr=l3
        while num3>0:
            newNode=ListNode(num3%10)
            curr.next=newNode
            curr=curr.next
            num3=num3//10
        return l3.next
            
        
        
        