# first access

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.tmp = defaultdict(int)
        self.count = 0

    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 

        if not root.left and not root.right:
            self.tmp[root.val] += 1
            # self.tmp.append(root.val)
            # print(self.tmp)
            cnt = 0
            for k,v in self.tmp.items():
                if v % 2 != 0:
                    cnt += 1
            if cnt <= 1 :
                self.count += 1
            
            self.tmp[root.val] -= 1
            # print(self.count)
            return self.count

        if root.left or root.right:
            self.tmp[root.val] += 1
            self.pseudoPalindromicPaths(root.left)
            self.pseudoPalindromicPaths(root.right) 
            self.tmp[root.val] -= 1
           
        
        return self.count




# revised access

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.tmp = defaultdict(int)
        self.count = 0

    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
          
        self.tmp[root.val] += 1

        if not root.left and not root.right:
            # self.tmp.append(root.val)
            # print(self.tmp)
            cnt = 0
            for k,v in self.tmp.items():
                if v % 2 != 0:
                    cnt += 1
            if cnt <= 1 :
                self.count += 1
 
        if root.left or root.right:
          
            self.pseudoPalindromicPaths(root.left)
            self.pseudoPalindromicPaths(root.right) 
         
        self.tmp[root.val] -= 1
        
        return self.count
