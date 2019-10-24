class node:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.val = x



class Treetraversal:

    def helper(self,root,res):
        if(root):
            if(root.left):
                self.helper(root.left,res)
            res.append(root.val)
            if(root.right):
                self.helper(root.right,res)
        return(res)
        
    def inordertreetraversal(self,root):
        res = []
        res = self.helper(root,res)
        return(res)



root = node(1)
root.left = node(null)
root.left.right=node(9)
root.right = node(12)
root.right.right=node(15)
t = Treetraversal()
print(t.inordertreetraversal(root))

