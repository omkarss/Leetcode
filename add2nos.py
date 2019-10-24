# Definition for singly-linked list.
import math
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1 ,l2):
        nos =  [] 
        rem = 0
        l3 = None
        
        if(l1 != None and l2!=None):
            temp = 0 
            temp = (l1.val + l2.val)%10
            l3 = ListNode(temp)
            rem= math.floor((l1.val + l2.val)/10)
            l1 = l1.next
            l2 = l2.next
        
        head = l3
        
        while(l1!=None and l2!=None):
            temp = 0 
            temp = (l1.val + l2.val)%10 
            tmpnode = ListNode(temp+rem)
            l3.next = tmpnode
            l3 = tmpnode
            rem = math.floor((l1.val + l2.val)/10)
            l1 = l1.next
            l2 = l2.next
        
        return head

        

    def printll(self, l1):
        while(l1!=None):
            print(l1.val)
            l1 = l1.next


ll = Solution()
head = ListNode(5)
head.next = ListNode(6)
head.next.next = ListNode(3)


head1 = ListNode(8)
head1.next = ListNode(4)
head1.next.next = ListNode(2)

head = ll.addTwoNumbers(head,head1)

ll.printll(head)
