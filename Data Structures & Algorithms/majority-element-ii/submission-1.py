class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        L=[]
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for num in freq:
            if freq[num] > len(nums)//3:
                L.append(num)
        return L
        