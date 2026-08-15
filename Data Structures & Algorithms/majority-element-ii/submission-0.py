class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i]=hashmap.get(i,0)+1
            else:
                hashmap[i]=1
        scores = [key for key, val in hashmap.items() if val > len(nums)/3]
        return scores