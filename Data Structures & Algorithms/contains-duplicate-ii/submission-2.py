class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen=set()
        n=len(nums)
        i,j=0,0
        while j<n:
            if abs(i-j)<=k:
                if nums[j] in seen:
                    return True
                else:
                    seen.add(nums[j])
                    j+=1
            else:
                seen.remove(nums[i])
                i+=1
        return  False