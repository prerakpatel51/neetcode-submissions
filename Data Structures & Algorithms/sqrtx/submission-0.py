class Solution:
    def mySqrt(self, x: int) -> int:
        low=1;high=x//2+1 
        if x==0:
            return 0
        while low<=high:
            mid=low+(high-low)//2
            if mid*mid==x :
                return mid
            if mid*mid<x :
                low=mid+1 
                if (mid+1)*(mid+1)>x:
                    return mid
            
            else:
                high=mid-1

            