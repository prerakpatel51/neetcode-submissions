class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        i=0;j=1
        duplicates=[]
        while j<len(nums):
            
            if nums[i]==nums[j]:
                duplicates.append(nums[j])
                print(duplicates)
            i+=1
            j+=1
            
           
        for i in duplicates:
            nums.remove(i)
        return len(nums)