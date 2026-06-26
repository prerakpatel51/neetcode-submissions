class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x=set()
        res=1
        for n in nums:
            x.add(n)
        for i in range(1,len(nums)+1):
            if i in x:
                res+=1
                continue
            else:
                return res
    
                
        return len(nums) + 1
