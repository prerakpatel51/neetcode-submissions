class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        prod=1
        i=0;j=len(nums)-1
        while i<len(nums):
           res.append(prod)
           print(prod)
           prod=nums[i] * prod
           i+=1 
        prod=1
        while j>=0:
            res[j]=res[j]*prod
            print(prod)
            prod=nums[j]*prod 
            j-=1
            
        return res
        
