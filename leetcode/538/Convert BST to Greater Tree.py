class Solution(object):
    def convertBST(self, root):
        self.curSum = 0

        def dfs(node):
            if node != None:
                dfs(node.right)
                self.curSum += node.val
                node.val = self.curSum
                dfs(node.left)
            
            return node

        

        return dfs(root)
