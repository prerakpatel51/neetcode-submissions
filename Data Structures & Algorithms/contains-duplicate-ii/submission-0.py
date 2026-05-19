class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        length=len(nums)
        for i in range(0,length):
            if nums[i] in d:
                if abs(i-d[nums[i]])<=k:
                    return True
            d[nums[i]]=i
        return False

       
            
            