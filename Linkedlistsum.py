#Definition for singly-linked list.
import math
class ListNode:
     def __init__(self, x):
         self.val = x
         self.forward = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        countl1 = 0
        countl2 = 0 
        curr = l1 
        next = l1.forward
        prev = None
        #reverse l1 
        while(next!=None):
            curr.forward = prev
            prev = curr 
            curr = next
            next = curr.forward
            countl1 = countl1 + 1
        
        curr.forward = prev
        l1 = curr
        
        
        curr = l2
        next = l2.forward
        prev = None
        #reverse l2 
        while(next!=None):
            curr.forward = prev
            prev = curr 
            curr = next
            next = curr.forward
            countl2 = countl2 + 1
        
        curr.forward = prev
        l2 = curr

        if (count1>count2):
            

        l3 = ListNode(0)
        temp = l3
        for _ in range(count):
            temp.forward = ListNode(0)
            temp = temp.forward
            
        rem = 0
        while(l1!=None):
            sum= (l1.val + l2.val+rem)%10
            rem = math.floor((l1.val + l2.val) /10)
            
            l3.val = sum
            l3 = l3.forward
            l2=l2.forward
            l1=l1.forward
            

        
        return temp
        
head1 = ListNode(3)
head1.forward = ListNode(4)
head1.forward.forward = ListNode(2)

head2 = ListNode(4)
head2.forward = ListNode(6)
head2.forward.forward = ListNode(5)


ll = Solution()
l3 = ll.addTwoNumbers(head1,head2)

while(l3!=None):
    print(l3.val)
    l3 = l3.forward