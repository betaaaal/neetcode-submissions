class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=[-1]*n
        right=[n]*n

        stack=[]

        # first smaller in right
        for i in range(n):
            while  stack and heights[stack[-1]]>heights[i]:
                right[stack[-1]]=i
                stack.pop()
            stack.append(i)

        stack=[]

        # first smaller in left
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>heights[i]:
                left[stack[-1]]=i
                stack.pop()
            stack.append(i)
        
        ans=0

        for i in range(n):
            width=right[i]-left[i]-1
            ans=max(ans, heights[i]*width)
        
        return ans