class Solution:
    def sum(self,l,r,nums):
        s=0
        for i in range(l,r+1):
            s+=nums[i]
        return s

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=r=0
        minlen=float('inf')
        for r in range(len(nums)):
            while self.sum(l,r,nums)>=target:
                length=r-l+1
                minlen=min(length,minlen)
                l+=1
        return minlen if minlen!=float('inf') else 0