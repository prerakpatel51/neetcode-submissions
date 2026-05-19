class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        i=0
        
        length=len(word1+word2)
        l1=len(word1)
        l2=len(word2)
        while len(res)<length:
        
            if i <l1:
                res.append(word1[i])
                
            
            if i<l2:
                res.append(word2[i])
            i+=1
        return ''.join(res)