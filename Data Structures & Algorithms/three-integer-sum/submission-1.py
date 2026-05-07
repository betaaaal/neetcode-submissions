class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(nums)):
            seen = {}

            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])

                if target in seen:
                    triplet = sorted([nums[i], nums[j], target])

                    if triplet not in res:
                        res.append(triplet)

                seen[nums[j]] = j

        return res
