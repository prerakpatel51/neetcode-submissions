class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0
        for i in range(0,len(heights)):
            while len(stack)!=0 and heights[stack[-1]]>heights[i]:
                element=stack[-1]
                stack.pop()
                nse=i
                pse=stack[-1] if len(stack)>0 else -1
                max_area=max(heights[element]*(nse-pse-1),max_area)
            stack.append(i)
        while len(stack)>0:
            element=stack[-1]
            stack.pop()
            pse=stack[-1] if len(stack)>0 else -1
            nse=len(heights)
            max_area=max(heights[element]*(nse-pse-1),max_area)


        return max_area