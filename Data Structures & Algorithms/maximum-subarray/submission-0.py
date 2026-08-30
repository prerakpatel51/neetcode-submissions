class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum=nums[0]
        sumi=0
        for i in nums:
            
            if sumi<0:
                sumi=0
            sumi+=i
            max_sum=max(sumi,max_sum)
            

        return max_sum
                
