class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(a,b):
            temp=a
            a=b
            b=temp
            return a,b

        for i in range(0,len(s)//2):
            l=i
            r=len(s)-1-i
            s[l],s[r]=swap(s[l],s[r])
        return s
        
