class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return True 
            if nums[mid]==nums[left]==nums[right]:
                left+=1
                right-=1
            # left side is sorted
            elif nums[left]<=nums[mid]:
                if target< nums[mid] and target>=nums[left]:
                    right=mid-1
                else:
                    left=mid+1
            # right side is sorted
            else:
                if target>nums[mid] and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return False
      