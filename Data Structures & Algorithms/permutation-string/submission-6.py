class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen={}
        for c in s1:
            if c in seen:
                seen[c]+=1
            else:
                seen[c]=1
        l=r=0
        for r in range(len(s2)):
            if s2[r] in seen:
                seen[s2[r]]-=1
            if r-l+1>len(s1):
                if s2[l] in seen:
                    seen[s2[l]]+=1
                l+=1
            count=0
            for key in seen:
                if seen[key]==0:
                    count+=1
            if count==len(seen):
                return True
        return False
