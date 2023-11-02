# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        global matchingSubTreeCount
        matchingSubTreeCount = 0

        def traversal(currentNode):
            
            global matchingSubTreeCount 

            if currentNode is None:
                return (0,0)    #(val,number)
            
            leftSubTree = traversal(currentNode.left)
            rightSubTree = traversal(currentNode.right)

            sumOfValues = leftSubTree[0] + rightSubTree[0] + currentNode.val
            countOfNodes = leftSubTree[1] + rightSubTree[1] + 1

            if countOfNodes != 0 and sumOfValues // countOfNodes == currentNode.val:
                matchingSubTreeCount += 1

            return (sumOfValues, countOfNodes)

        traversal(root)

        return matchingSubTreeCount
