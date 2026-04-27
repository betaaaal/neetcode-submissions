class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L=[]
        for i in range(0,len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    L.append(i)
                    L.append(j)
        return L