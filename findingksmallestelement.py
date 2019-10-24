class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    array=[]
    def KthElement(self,root,k):
        if(root == None):
            return
        else:
            self.KthElement(root.left,k)
            self.array.append(root.val)
            self.KthElement(root.right,k)



    def kthSmallest(self, root, k):
            self.arr = []
            self.count = 0
            self.KthElement(root,k)
            return self.array[k-1]






s = Solution()
head1 = TreeNode(4)
head1.left = TreeNode(2)
head1.left.right = TreeNode(3)
head1.left.left = TreeNode(1)
#head1.left.left.left = TreeNode(1)
#head1.left.right = TreeNode(4)
#head1.left.right.left = TreeNode(1)
#head1.left.right.left.left = TreeNode(7)
head1.right = TreeNode(5)

#head1.right = TreeNode(7)
#head1.right.left = TreeNode(3)
#head1.right.right = TreeNode(2)
print(s.kthSmallest(head1,5))