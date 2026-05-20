class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        charhashs2=[0]*26
        charhashs1=[0]*26
        
        left=0
        for i in s1:
            charhashs1[ord(i)-ord('a')]+=1
        for right in range(len(s2)):
            charhashs2[ord(s2[right])-ord('a')]+=1
            if right-left+1>len(s1):
                charhashs2[ord(s2[left])-ord('a')]-=1
                left+=1
            
         
            if charhashs1==charhashs2:
                return True
        return False


                
