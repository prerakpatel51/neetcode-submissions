class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res=0
        currsum=sum(arr[:k-1])
        for i in range(len(arr)-k+1):
            currsum+=arr[i+k-1]
            if (currsum/k)>=threshold:
                res+=1
            currsum-=arr[i]
            
        return res
            
        
        