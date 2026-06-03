class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix) #rows
        n=len(matrix[0]) # columns
        row=-1
        low, high=0, m-1
        while low<=high:
            mid=(low+high)//2
            if matrix[mid][0]<=target<=matrix[mid][n-1]:
                row=mid
                break
            elif matrix[mid][0]>target:
                high=mid-1
            else:
                low=mid+1

        if row==-1:
            return False
        
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]<target:
                low=mid+1
            else:
                high=mid-1
        return False