class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0;j=0;
        while i<len(haystack):
            if haystack[i]==needle[j]:
                print(haystack[i], "matched", needle[j])
                if j==len(needle)-1:
                    return i-j
                if i<len(haystack)-1 and j<len(needle)-1:
                    i+=1;
                    j+=1;
              
            if haystack[i]!=needle[j]:
                j=0
                if i<len(haystack):
                    i+=i-j+1;
            
        return -1


