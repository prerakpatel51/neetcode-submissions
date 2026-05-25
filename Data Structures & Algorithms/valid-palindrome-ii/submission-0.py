class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(k):
            i=0;j=len(k)-1;
            while i<=j:
                if k[i]!=k[j]:
                    return False
                i+=1
                j-=1
            return True
        if is_palindrome(s)==True:
            return True
        else:
            for i in range(0,len(s)):
                new_s = s.replace(s[i], "", 1)
                if is_palindrome(new_s)==True:
                    return True
        return False