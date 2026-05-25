class Solution:
    def isValid(self, s: str) -> bool:
        openning=['(','{','[']
        closing=[')','}',']']
        stack=[]
        for i in s:
            if i in openning:
                stack.append(i)
                print(stack)
                print("\n")
                continue
            if i in closing:
                if i==')' and stack[-1]=='(':
                    stack.pop()
                    print(stack)
                    print("\n")
                    continue
                if i=='}' and stack[-1]=='{':
                    stack.pop()
                    print(stack)
                    print("\n")
                    continue
                if i==']' and stack[-1]=='[':
                    stack.pop()
                    print(stack)
                    print("\n")
                    continue
                else:
                    return False
        
        if len(stack)==0:
            return True
