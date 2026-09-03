class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
         
        def CanWeSplit(m):
            ts=0
            n=1
            max_sum=0
            for i in nums:
                if ts+i>m:
                    ts=i
                    n+=1

                else:
                    ts+=i
                max_sum=max(max_sum,ts)
            if n<=k:
                return (True , max_sum)
            else: 
                return (False,max_sum)

                
                
           

        lw=max(nums)
        hw=sum(nums)
        d=0
        ans=0
        while lw<=hw :
            m=(lw+hw)//2
            if CanWeSplit(m)[0]:
                ans=CanWeSplit(m)[1]
                hw=m-1
            else:
                lw=m+1
        return ans
            
            



