class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        f=k%len(nums)
        for _ in range(0,f):
            
            e=nums.pop()

            nums.insert(0,e)

