class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def calcBFS(self,root):

        if(not root):
            return []

        nodes=[]
        nodes.append(root)
        op=[]
        arr =[root.val]

        level = 0
        count = 0
        flag = True

        while(len(nodes) > 0):



            if(flag == True):
                break


            if(count==0):
                op.append(arr)
                level = level + 1
                count = 2 ** level
                arr = []

            node = nodes.pop(0)

            if(node == None):
                nodes.append(None)
                nodes.append(None)
                count = count - 2
                continue


            if(node.left!=None):
                nodes.append(node.left)
                arr.append(node.left.val)
            else:
                nodes.append(None)

            if(node.right!=None):
                nodes.append(node.right)
                arr.append(node.right.val)
            else:
                nodes.append(None)


            count = count - 2






        return op



    def levelOrder(self, root):
        nodes = [[]]
        return(self.calcBFS(root))







s = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
#root.right= TreeNode(3)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.left.left = TreeNode(5)


#root.left.right = TreeNode(None)
#root.right.left = TreeNode(None)
#root.right.right = TreeNode(5)


print(s.levelOrder(root))


#[1,2,null,3,null,4,null,5]
