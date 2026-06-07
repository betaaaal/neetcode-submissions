class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # Helper function to check if a max sum capacity is feasible
        def canSplit(max_sum: int) -> bool:
            subarray_count = 1
            current_sum = 0
            
            for num in nums:
                if current_sum + num > max_sum:
                    # Start a new subarray
                    subarray_count += 1
                    current_sum = num
                    # If we exceed the allowed number of splits, it's invalid
                    if subarray_count > k:
                        return False
                else:
                    current_sum += num
            return True

        # Initialize binary search boundaries
        low = max(nums)
        high = sum(nums)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if canSplit(mid):
                ans = mid          # Track the valid minimized maximum sum
                high = mid - 1     # Try to find a smaller maximum sum
            else:
                low = mid + 1      # Increase the allowed maximum sum
                
        return ans