class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(1,len(nums)+1):
            if i not in nums:
                return i
        else:
            return len(nums)+1

