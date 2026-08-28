# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pow1=0
        num1=0
        curr1=l1
        pow2=0
        num2=0
        curr2=l2
        while curr1:
            num1=num1+(curr1.val * (10**pow1))
            pow1+=1
            curr1=curr1.next

        while curr2:
            num2=num2+(curr2.val * (10**pow2))
            pow2+=1
            curr2=curr2.next
        ans=str(num1+num2)
        dummy = ListNode(0)
        curr = dummy
        for s in ans[::-1]:
            curr.next = ListNode(int(s))
            curr = curr.next
        return dummy.next

            