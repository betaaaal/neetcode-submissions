from typing import List, Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next


    def partitionAndMerge(self, start, end, lists):
        if start > end:
            return None

        if start==end:
            return lists[start]

        mid=(start+end)//2
        left=self.partitionAndMerge(start, mid, lists)
        right=self.partitionAndMerge(mid+1, end, lists)
        return self.mergeTwoLists(left, right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        return self.partitionAndMerge(0, len(lists)-1, lists)