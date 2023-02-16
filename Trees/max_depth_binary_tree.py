
'''

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

'''

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val



class Solution:
    def maxDepth(self, root):
        
        def _maxDepth(root):
            if not root:
                return 0 
            else:
                l = _maxDepth(root.left) + 1
                r = _maxDepth(root.right) + 1

                return max(l, r)
        
        return _maxDepth(root)

t = TreeNode(3)
t.right = TreeNode(20)
t.left = TreeNode(9)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

s = Solution()
print(s.maxDepth(t))