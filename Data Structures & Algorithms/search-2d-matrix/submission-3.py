class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        low=0;high=len(matrix)-1
      
        while low<=high:
            mid=(low+high)//2
            
            if target >=matrix[mid][0] and target<=matrix[mid][-1]:
                l=0;r=len(matrix[mid])-1 
                while l<=r:
                    m=(l+r)//2
                    if target==matrix[mid][m]:
                        return True
                    if target>matrix[mid][m]:
                        l=m+1
                    else:
                        r=m-1 
            if target>matrix[mid][-1]:
                low=mid+1
            else:
                high=mid-1    
 
                
        return False
                


        
        # for i in matrix:
        #     low,high=0,len(i)-1
        #     while low<=high:
        #         mid=low+(high-low)//2
        #         if i[mid]==target:
        #             return True
        #         if i[mid]<target:
        #             low=mid+1
        #         else:
        #             high=mid-1
        # return False
            