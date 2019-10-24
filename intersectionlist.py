class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self,head1,head2):
        nodes_dict = {}

        if(head1 == None or head2 == None):
            return None


        while(head1):
            nodes_dict[head1.val] = head1
            head1 = head1.next

        while(head2):
            if(head2.val in nodes_dict.keys()):
                if(nodes_dict[head2.val] == head2):
                    return head2.val
            head2 = head2.next
        return None







s = Solution()
head1 = ListNode(0)
head1.next = ListNode(9)
head1.next.next= ListNode(1)
head1.next.next.next = ListNode(2)
head1.next.next.next.next = ListNode(4)
#head1.next.next.next.next.next = ListNode(6)
#head1.next.next.next.next.next.next = ListNode(7)


head2 = ListNode(3)
head2.next = head1.next.next.next
#head2.next.next= ListNode(4)
#head2.next.next.next = head1.next.next



print(s.getIntersectionNode(head1,head2))
