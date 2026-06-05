class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ops=["+","-","*","/"]
        for t in tokens:
            if t in ops:
                b=int(stack.pop())
                a=int(stack.pop())
                if t==ops[0]:
                    stack.append(a+b)
                elif t==ops[1]:
                    stack.append(a-b)
                elif t==ops[2]:
                    stack.append(a*b)
                elif t==ops[3]:
                    stack.append(int(a/b))
                  

            else:
                stack.append(int(t))
        return stack[0]