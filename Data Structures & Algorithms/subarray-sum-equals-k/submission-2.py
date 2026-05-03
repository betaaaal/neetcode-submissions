class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap=defaultdict(int)
        prefixSum=0
        hashMap[0]=1
        result=0
        for i in range(0,len(nums)):
            prefixSum+=nums[i]
            if prefixSum-k in hashMap:
                result+=hashMap[prefixSum-k]
            hashMap[prefixSum]+=1
        return result


