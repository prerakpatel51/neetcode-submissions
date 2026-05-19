class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(0,len(nums)):
            difference=target-nums[i]
            if difference in h:
                return [h.get(difference),i]
            else: 
                h[nums[i]]=i