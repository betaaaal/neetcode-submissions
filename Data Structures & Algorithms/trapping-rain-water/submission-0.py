class Solution:
    def glm(self,height,n):
        leftMax=[0]*n
        leftMax[0]=height[0]
        for i in range(1,n):
            leftMax[i]=max(leftMax[i-1],height[i])
        return leftMax
    def grm(self,height,n):
        rightMax=[0]*n
        rightMax[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            rightMax[i]=max(rightMax[i+1],height[i])
        return rightMax

    def trap(self, height: List[int]) -> int:
        n=len(height)
        leftMax=self.glm(height,n)
        rightMax=self.grm(height,n)
        sum=0
        for i in range(0,n):
            h=min(leftMax[i],rightMax[i])-height[i]
            sum+=h
        return sum