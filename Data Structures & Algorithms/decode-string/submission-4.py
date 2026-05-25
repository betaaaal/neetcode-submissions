class Solution:
    def decodeString(self, s: str) -> str:
        nstack=[]
        sstack=[]
        num=''
        for s1 in s:
            if s1.isdigit():
                num+=s1
            elif s1=='[':
                nstack.append(int(num))
                num=''
                sstack.append(s1)
            elif s1!=']':
                sstack.append(s1)
            elif s1==']':
                x=[]
                while sstack[-1]!='[':
                    x.append(sstack.pop())
                x.reverse()
                sstack.pop()
                decoded=''.join(x)
                sstack.append(decoded*nstack.pop())
        return ''.join(sstack) 
