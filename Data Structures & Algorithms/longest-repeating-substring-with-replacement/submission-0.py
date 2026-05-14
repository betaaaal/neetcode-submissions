class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            freq={}
            for j in range(i,n):
                ch=s[j]
                if ch in freq:
                    freq[ch]+=1
                else:
                    freq[ch]=1
                maxfreq=0
                for v in freq.values():
                    if v > maxfreq:
                        maxfreq=v
                length=j-i+1
                replacements=length-maxfreq
                if replacements<=k:
                    ans=max(ans, length)
        return ans