class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums=[]
        i,j=0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i]<=nums2[j]:
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1
        nums.extend(nums1[i:])
        nums.extend(nums2[j:])
        if len(nums)%2!=0:
            return nums[len(nums)//2]
        else:
            a=len(nums)//2
            return (nums[a]+nums[a-1])/2
