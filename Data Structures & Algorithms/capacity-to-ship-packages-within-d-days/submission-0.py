class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low,high=max(weights), sum(weights)
        ans=high
        while low<=high:
            mid=(low+high)//2
            days_needed=1
            current_load=0
            for w in weights:
                if current_load+w <= mid:
                    current_load+=w
                else:
                    days_needed+=1
                    current_load=w
            if days_needed<=days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans