class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini=float('inf')


    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.stack.append(val)
            self.mini=val
        elif val>=self.mini:
            self.stack.append(val)
        else:
            self.stack.append(2*val-self.mini)
            self.mini=val
    


    def pop(self) -> None:
        x=self.stack[-1]
        
        if x<self.mini:
            self.mini=2*self.mini-x
       
        self.stack.pop()
        if len(self.stack)==0:
            self.mini=float('inf')
            
        

    def top(self) -> int:
        if self.mini>self.stack[-1]:
            return self.mini
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.mini
