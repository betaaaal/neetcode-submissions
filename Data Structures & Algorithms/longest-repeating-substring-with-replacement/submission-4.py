class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        l=0
        ans=0
        freq={}
        maxfreq=0
        for r in range(n):
            ch=s[r]
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
            maxfreq=max(maxfreq,freq[ch])
            length=r-l+1
            replacements=length-maxfreq
            if replacements>k:
                l+=1
                freq[s[l-1]]-=1
            length=r-l+1
            ans=max(ans, length)
        return ans