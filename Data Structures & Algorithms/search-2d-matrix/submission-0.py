class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            low,high=0,len(i)-1
            while low<=high:
                mid=low+(high-low)//2
                if i[mid]==target:
                    return True
                if i[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
        return False
            