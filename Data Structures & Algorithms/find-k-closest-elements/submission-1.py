class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        hmm=[]
        for i in arr:
            hmm.append((abs(i-x),i))
        hmm.sort()
        l=[]
        for i in range(k):
            l.append(hmm[i][1])
        return sorted(l)
        
