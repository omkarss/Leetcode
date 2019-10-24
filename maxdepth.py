# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    max_height = 0
    def getmaxdepth(self,root,height):
        if(root == None):
            return height
        else:
            if(self.max_height<height):
                self.max_height = height
            height = height + 1
            return(max(self.getmaxdepth(root.left,height),self.getmaxdepth(root.right,height)))


    def maxDepth(self,root):
        if(root == None):
            return 0
        self.getmaxdepth(root,0)
        return self.max_height+1



s = Solution()
head1 = TreeNode(4)
head1.left = TreeNode(8)
#head1.left.left = Node(7)
#head1.left.right = TreeNode(9)
#head1.left.right.left = TreeNode(1)
#head1.left.right.left.left = TreeNode(7)

#head1.right = TreeNode(7)
#head1.right.left = TreeNode(3)
#head1.right.right = TreeNode(2)

print(s.maxDepth(head1))


