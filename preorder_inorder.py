class ListNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)


def search_index(val, inorder):

    for i in range(0,len(inorder)):
        if inorder[i] == val:
            return i
    else:
        return -1



def preorderinorder(preorder,inorder,start,end):
    if(start>end or start<0 or len(inorder)<1):
        return



    root = ListNode(preorder[preorderinorder.pre_index])
    preorderinorder.pre_index = preorderinorder.pre_index+1

    if(start == end):
        return root



    inorder_ind = search_index(root.val,inorder)

    root.left = preorderinorder(preorder,inorder,start,inorder_ind-1)

    root.right = preorderinorder(preorder,inorder,inorder_ind+1,end)

    return root




preorderinorder.pre_index =0


head1 = ListNode(1)
head1.left = ListNode(9)
head1.left.left = ListNode(12)
head1.left.right = ListNode(11)
head1.right = ListNode(20)
head1.right.left = ListNode(15)
head1.right.right = ListNode(7)

print(preorderinorder([10,2,3,4,7,5,6],[3,2,4,10,5,7,6],0,len([3,2,4,10,5,7,6])-1))