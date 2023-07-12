q1>class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_subtree_sum(root):
    if root is None:
        return 0

    # Calculate the sum of the current subtree
    subtree_sum = root.val + max_subtree_sum(root.left) + max_subtree_sum(root.right)

    # Compare the current subtree sum with the maximum sum found so far
    if hasattr(max_subtree_sum, 'max_sum'):
        max_subtree_sum.max_sum = max(max_subtree_sum.max_sum, subtree_sum)
    else:
        max_subtree_sum.max_sum = subtree_sum

    return subtree_sum

# Example usage
# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Find the subtree with the maximum sum
max_subtree_sum(root)

# Print the maximum sum
print(max_subtree_sum.max_sum)




q2>class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def construct_bst(level_order):
    if not level_order:
        return None

    # Create the root node from the first element
    root = TreeNode(level_order[0])

    # Find the index of the first element greater than the root
    index = 1
    while index < len(level_order) and level_order[index] < root.val:
        index += 1

    # Recursively construct the left and right subtrees
    root.left = construct_bst(level_order[1:index])
    root.right = construct_bst(level_order[index:])

    return root

def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# Example usage
level_order = [7, 4, 12, 3, 6, 8, 1, 5, 10]

# Construct the BST
root = construct_bst(level_order)

# Perform inorder traversal to verify the BST
inorder = inorder_traversal(root)

# Print the inorder traversal
print(inorder)





q3>def is_valid_level_order(arr):
    n = len(arr)

    # Edge case: Empty array or single element is a valid BST
    if n <= 1:
        return True

    # Find the index of the first element greater than the root
    index = 1
    while index < n and arr[index] < arr[0]:
        index += 1

    # All elements after index should be greater than the root
    for i in range(index, n):
        if arr[i] < arr[0]:
            return False

    # Recursively check if the left and right subtrees are valid BSTs
    left_valid = is_valid_level_order(arr[1:index])
    right_valid = is_valid_level_order(arr[index:])

    # Return True if both subtrees are valid BSTs
    return left_valid and right_valid

# Example usage
arr1 = [7, 4, 12, 3, 6, 8, 1, 5, 10]
arr2 = [11, 6, 13, 5, 12, 10]

# Check if arr1 represents a valid BST
valid1 = is_valid_level_order(arr1)
print(valid1)  # Output: True

# Check if arr2 represents a valid BST
valid2 = is_valid_level_order(arr2)
print(valid2)  # Output: False
