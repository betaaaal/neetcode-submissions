class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r=0,len(arr)-1
        while r-l+1>k:
            if abs(x-arr[l]) > abs(x-arr[r]): 
                l+=1 #When two numbers are equally close:choose the smaller element
            else:
                r-=1
        return arr[l:r+1]

        
