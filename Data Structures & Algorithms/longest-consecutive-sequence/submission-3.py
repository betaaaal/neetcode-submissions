class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        max_count=0
        for i in range(0,n):
            num=nums[i]
            count=1
            while num+1 in nums:
                count+=1
                num+=1
            max_count=max(count, max_count)
        return max_count

            

        