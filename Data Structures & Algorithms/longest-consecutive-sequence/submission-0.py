class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        if not nums:
            return 0
        num_set=set(nums)
        for num in num_set:
            if num-1 not in num_set:
                j=num
                while j in num_set:
                    
                    j+=1
                current_streak=j-num
                longest=max(current_streak,longest)  
        return longest

        