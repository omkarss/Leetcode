# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def oddEvenList(self, head):

        if(head.next==None):
            return head

        evenhead = even = head.next

        odd  = odds = head

        #1->2->3->4->5

        while(odd.next and even.next):
            odd.next = even.next #1->3
            odd = odd.next
            even.next = odd.next
            even = even.next


        if(odd.next):
            odd.next = evenhead

        else:
            odd.next = evenhead

        return odds




s = Solution()
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next= ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
head1.next.next.next.next.next = ListNode(6)
head1.next.next.next.next.next.next = ListNode(7)




head = s.oddEvenList(head1)

while(head!=None):
    print(head.val)
    head=head.next




