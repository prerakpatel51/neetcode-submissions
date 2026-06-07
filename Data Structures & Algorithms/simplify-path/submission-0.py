class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=path.split('/')
        # print(stack)
        res=[]
        for i in stack:
            if i=='':
                continue
            if i=='.':
                continue
            elif i=="..":
                if res:
                    res.pop()
            else:
               
                
                res.append(i)

        final_res="/"+"/".join(res)
        
        return final_res