
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={} 
        freq=[[] for i in range(len(nums)+1)]
        print(freq)
        #key is the number of times 
        # a value occur and values will be the list of the elements that occur
        for i in nums:
            count[i]=count.get(i,0)+1
        print(count)
        for n,c in count.items():
            freq[c].append(n)
        print(freq)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

