# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:
        trees = {}
        count = {}
        result = []

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            key = (node.val, left, right)

            if key not in trees:
                trees[key] = len(trees) + 1

            tree_id = trees[key]
            count[tree_id] = count.get(tree_id, 0) + 1

            if count[tree_id] == 2:
                result.append(node)

            return tree_id

        dfs(root)
        return result
