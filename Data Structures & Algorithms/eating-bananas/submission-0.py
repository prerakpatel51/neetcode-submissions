import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        high = max(piles)
        ans=high
        while l <= high:
            mid = (l + high) // 2
            i = 0
            hours = 0
            while i < len(piles):
                hours += math.ceil(piles[i] / mid) 
                i += 1
            if hours<=h:
                ans=mid
                high=mid-1
            else:
                l=mid+1
        return ans
            

        
