class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq=dict()
        for i in range(0,len(nums)):
            if freq.get(nums[i]) is None:
                freq[nums[i]]=1
            else:
                return True
        return False
        