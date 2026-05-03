class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=[]
        s2=[]
        for i in range(0,len(s)):
            s1.append(s[len(s)-1-i])
            s2.append(s[i])
        s3=[]
        for i in range(0,len(s2)):
            if s2[i].isalnum() == True:
                s3.append(s2[i].lower())
        s4=[]
        for i in range(0,len(s1)):
            if s1[i].isalnum() == True:
                s4.append(s1[i].lower())
        return s3==s4