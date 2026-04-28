class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        for i in range(0,len(nums)):
            prod=1
            for j in range(0,len(nums)):
                if i!=j:
                    prod*=nums[j]
            prefix[i]=(prod)
        return prefix



            