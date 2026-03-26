# Subtree of Another Tree
# Given two binary trees, check if subRoot is a subtree of root.
# A subtree must have the exact same structure and node values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Check if two trees are identical
def same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val and
            same_tree(p.left, q.left) and
            same_tree(p.right, q.right))

# Check if subRoot exists as a subtree in root
def is_subtree(root, sub_root):
    if not root:
        return False
    if same_tree(root, sub_root):
        return True
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)

# Example 1: root = [3,4,5,1,2], subRoot = [4,1,2] -> true
root1 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
sub1 = TreeNode(4, TreeNode(1), TreeNode(2))
print(is_subtree(root1, sub1))  # True

# Example 2: root = [3,4,5,1,2(->0),null,null], subRoot = [4,1,2] -> false
root2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
sub2 = TreeNode(4, TreeNode(1), TreeNode(2))
print(is_subtree(root2, sub2))  # False
