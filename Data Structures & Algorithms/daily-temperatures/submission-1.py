class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result=[0]*n
        stack=[]
        for idx in range(n-1,-1,-1):
            # top element is less than or equal to idx
            while stack and temperatures[stack[-1]]<= temperatures[idx]:
                stack.pop()
            if stack:
                result[idx]=stack[-1]-idx
            stack.append(idx)
        return result