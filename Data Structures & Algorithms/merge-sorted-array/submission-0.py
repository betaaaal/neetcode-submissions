class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(1,n+1):
            nums1[-i]=nums2[-i]

        for i in range(0,m+n+1):
            for j in range(i+1,m+n):
                if nums1[j]<nums1[i]:
                    nums1[i], nums1[j]=nums1[j],nums1[i]
