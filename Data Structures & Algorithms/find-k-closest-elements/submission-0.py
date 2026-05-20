class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff=[[abs(num-x),num] for num in arr ]
        res=[]
        diff.sort()
 
        for i in range(k):
            res.append(diff[i][1])
        return sorted(res)