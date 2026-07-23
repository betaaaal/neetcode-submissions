class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k-1
        L=[]
        while r<len(nums):
            m=max(nums[l:r+1])
            L.append(m)
            l+=1
            r+=1
        return L
