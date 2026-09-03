class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def CanWeShip(m):
            ts=0
            d=1
            for i in weights:

                
                if ts+i>m:
                    d+=1
                    ts=i
                else:
                    ts+=i
                    
            return d

        lw=max(weights)
        hw=sum(weights)
        d=0
        ans=0
        while lw<=hw :
            m=(lw+hw)//2
            if CanWeShip(m)<=days:
                ans=m
                hw=m-1
            else:
                lw=m+1
        return ans
            
            







        