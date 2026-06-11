class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        left=0
        right=mountainArr.length() - 1
        while left<right:
            mid=(left+right)//2
            if mountainArr.get(mid)<mountainArr.get(mid+1):
                left=mid+1
            else:
                right=mid
        m=left
        left=0
        right=m
        while left<=right:
            mid=(right+left)//2
            if mountainArr.get(mid)==target:
                return mid
            elif mountainArr.get(mid)>target:
                right=mid-1
            else:
                left=mid+1
        right=mountainArr.length()-1
        left=m+1
        while left<=right:
            mid=(left+right)//2
            if mountainArr.get(mid)==target:
                return mid
            elif mountainArr.get(mid)>target:
                left=mid+1
            else:
                right=mid-1
        return -1