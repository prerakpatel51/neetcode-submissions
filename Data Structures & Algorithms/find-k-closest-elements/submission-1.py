import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap=[]
        for num in arr:
            dist=abs(num-x)
            heapq.heappush(max_heap,(-dist,-num))
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        res=[-num for (dist,num) in max_heap]
        return sorted(res)