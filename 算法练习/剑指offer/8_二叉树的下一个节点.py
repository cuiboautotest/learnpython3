'''
给定一个二叉树和其中的一个节点，请找出中序遍历顺序的下一个节点并且返回。注意，树中的节点不仅包含左右子节点，同时包含指向父节点的指针。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.father = None
class Solution:
    def inorderSuccessor(self, q):
        if not q: return None
        if q.right:
            q = q.right
            while q.left:
                q = q.left
            return q
        while q.father and q.father.right == q:
            q = q.father
        return q.father
