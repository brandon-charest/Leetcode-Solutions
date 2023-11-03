from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# time: O(n)
# space: O(h) where h is the height of the tree
def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    self.res = 0

    def search(node):
        if not node:
            return (0, 0)

        l_val, l_children = search(node.left)
        r_val, r_children = search(node.right)
        sub_tree = l_children + r_children + 1
        total = l_val + r_val + node.val
        average = total // sub_tree

        if average == node.val:
            self.res += 1

        return (total, sub_tree)

    search(root)
    return self.res
