class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class  Solution:

    def isValidBST(self, root):
        arr=[]
        arr =self.is_helper(root,arr)
        for i in range(1,len(arr)):
            if(arr[i]<arr[i-1]):
                return False
        return True



    def is_helper(self, root, arr):
        if(root):
            self.is_helper(root.left,arr)
            arr.append(root.val)
            self.is_helper(root.right,arr)
        return arr


s = Solution()

root = TreeNode(2)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
#root.left.left.left = TreeNode()
#root.left.left.left.left = TreeNode(5)
#root.right.left = TreeNode(3)
#root.right.right = TreeNode(6)

print(s.isValidBST(root))


