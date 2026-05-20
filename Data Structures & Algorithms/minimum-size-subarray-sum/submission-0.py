class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        min_sub=float('inf')
        cursum=0
        for r in range(len(nums)):
            cursum+=nums[r]
            while cursum>=target:
                min_sub=min(min_sub,r-l+1)
                cursum-=nums[l] 
                l+=1
        return 0 if min_sub==float('inf') else min_sub
            