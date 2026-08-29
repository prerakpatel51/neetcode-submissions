# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        curr=head
        while curr:
            length+=1
            curr=curr.next
        index=length-n
        if index == 0:
            return head.next
        curr1=head
       
        for i in range(index-1):
            curr1=curr1.next
        if curr1.next:    
            curr1.next=curr1.next.next
        else:
            curr1.next=None

        return head
            