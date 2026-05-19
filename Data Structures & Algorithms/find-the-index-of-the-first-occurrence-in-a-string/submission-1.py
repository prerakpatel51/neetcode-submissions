class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0;j=0;
        while i<len(haystack):
            if haystack[i]==needle[j]:
                print(haystack[i], "matched", needle[j])
                if j==len(needle)-1:
                    return i-j
                i+=1;
                j+=1;
              
            elif haystack[i]!=needle[j]:
                i=i-j+1;
                j=0;
        return -1