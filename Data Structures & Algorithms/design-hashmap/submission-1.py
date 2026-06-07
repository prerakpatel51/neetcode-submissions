class Node:
    def __init__(self,val):
        self.val=[val[0],val[1]]
        self.next=None
class MyHashMap:

    def __init__(self):
        self.set=[Node([0,0]) for i in range(10**3)]


    def put(self, key: int, value: int) -> None:
        curr=self.set[key%len(self.set)]
        while curr.next:
            if curr.next.val[0]==key:
                curr.next.val[1]=value
                return
            curr=curr.next
        curr.next=Node([key,value])
       


    def get(self, key: int) -> int:
        curr=self.set[key%len(self.set)]
        while curr.next:
            if curr.next.val[0]==key:
                
                return curr.next.val[1]
            curr=curr.next
        return -1

    def remove(self, key: int) -> None:
        curr=self.set[key%len(self.set)]
        while curr.next:
            if curr.next.val[0]==key:
                curr.next=curr.next.next
                return
            curr=curr.next
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)