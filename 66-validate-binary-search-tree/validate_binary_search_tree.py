# Validate Binary Search Tree
# Given a binary tree, determine if it is a valid BST.
# Each node must be within an allowed range (min, max) that updates as we go deeper.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(node, min_val=float("-inf"), max_val=float("inf")):
    # An empty node is always valid
    if not node:
        return True

    # Check if current node is within its allowed range
    if node.val <= min_val or node.val >= max_val:
        return False

    # Left child must be less than current node (update max)
    # Right child must be greater than current node (update min)
    return (is_valid_bst(node.left, min_val, node.val) and
            is_valid_bst(node.right, node.val, max_val))

# Example 1: [2,1,3] -> true
tree1 = TreeNode(2, TreeNode(1), TreeNode(3))
print(is_valid_bst(tree1))  # True

# Example 2: [5,1,4,null,null,3,6] -> false
tree2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(is_valid_bst(tree2))  # False
