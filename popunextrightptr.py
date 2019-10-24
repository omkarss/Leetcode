class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None




class Solution:
    def connect(self, root):

        arr = []
        arr.append(root)

        while(len(arr)>0):
            l = len(arr)
            for i in range(0,l):
                if(arr[i] != None):
                    if(i+1<l):
                        if(arr[i+1]!=None):
                            arr[i].next = arr[i+1]
                        else:
                            arr[i].next=None
                    else:
                        arr[i].next = None

            for i in range(0,l):
                if(arr[0] == None or ((arr[0].left) ==None and (arr[0].right)==None)):
                    arr.pop(0)
                else:
                    pop_ele = arr.pop(0)
                    arr.append(pop_ele.left)
                    arr.append(pop_ele.right)


        return root



s = Solution()
head1 = Node(4)
#head1.left = Node(5)
#head1.left.left = Node(7)
#head1.left.right = Node(8)
#head1.right = Node(6)
#head1.right.left = Node(9)
#head1.right.right = Node(10)


root = s.connect(head1)
