class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dicti={}
        for n in nums:
            if n not in dicti:
                dicti[n]=1
            else:
                dicti[n]+=1
        for key in dicti:
            if dicti[key]>1:
                return key