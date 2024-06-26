# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        nums = []

        def inorder(node, nums):
            '''
            Convert BST to ascending sequence
            '''

            if node != None:
                inorder(node.left, nums)
                nums.append(node.val)
                inorder(node.right, nums)

        def sequence_to_balanced_BST(left, right, nums):

            '''
            Convert ascending sequence to balanced BST
            '''

            if left > right:

                return None

            else:

                mid = left + (right - left) // 2

                root = TreeNode(nums[mid])

                root.left = sequence_to_balanced_BST(left, mid - 1, nums)
                root.right = sequence_to_balanced_BST(mid + 1, right, nums)

                return root

        inorder(root, nums)
        # print(nums)
        return sequence_to_balanced_BST(0, len(nums) - 1, nums)