class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(0,len(nums)-2):
            k=i+1
            j=len(nums)-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while(k<j):
                if nums[k]+nums[j]==-nums[i]:
                    res.append([nums[k],nums[j],nums[i]])
                    k+=1
                    j-=1
                    while k < j and nums[k] == nums[k - 1]:
                        k += 1

                    while k < j and nums[j] == nums[j + 1]:
                        j -= 1
                  
                if nums[k]+nums[j]<-nums[i]:
                    k+=1
                   
                if nums[k]+nums[j]>-nums[i]:
                    j-=1
        return res