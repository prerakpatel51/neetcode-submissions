class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        i=0
        while i<32:
            res=res+n%2
            n=n//2
            i+=1
        return res
        
        
        
