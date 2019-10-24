# Definition for singly-linked list.
import math
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    head1 = None
    head2 = None
    l1_len1 =0
    l2_len2 = 0

    def addTwoNumbers(self, l1, l2):
        self.head1 = l1
        self.head2 = l2
        temp1 = self.head1
        temp2 = self.head2


        while(True):
            if(self.head1.next):
                self.head1 = self.head1.next
                self.l1_len1 = self.l1_len1 + 1
            else:
                self.l1_len1 = self.l1_len1 + 1
                break


        while(True):
            if(self.head2.next):
                self.head2=self.head2.next
                self.l2_len2 = self.l2_len2 + 1
            else:
                self.l2_len2 = self.l2_len2 + 1
                break
        temp1 = l1
        temp2 = l2

        l1= self.head1
        l2= self.head2

        while(self.l1_len1 != self.l2_len2):
            if(self.l1_len1 > self.l2_len2) :
                temp = ListNode(0)
                l2.next = temp
                l2= l2.next
                self.l2_len2 =  self.l2_len2 + 1

            elif(self.l2_len2 > self.l1_len1):
                temp = ListNode(0)
                l1.next = temp
                l1 = l1.next
                self.l1_len1 = self.l1_len1 + 1



        l3 = ListNode(temp1.val + temp2.val)
        head3 = l3
        rem = 0

        if(temp1.next):
            temp1 = temp1.next

        if(temp2.next):
            temp2 = temp2.next

        while(temp1):

            temp = 0
            temp =  (temp1.val + temp2.val) % 10
            tmpnode = ListNode(temp + rem)
            l3.next = tmpnode
            l3 = tmpnode
            rem = int(math.floor((temp1.val + temp1.val) / 10))
            temp1 = temp1.next
            temp2 = temp2.next




        return head3















s = Solution()
head1 = ListNode(2)
head1.next = ListNode(3)
head1.next.next= ListNode(4)

head2 = ListNode(4)
head2.next = ListNode(5)
head2.next = ListNode(7)

s.addTwoNumbers(head1,head2)

