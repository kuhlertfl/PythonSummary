# =============================================================================
# Binary Search Tree (BST) in Python
# =============================================================================

# A Binary Search Tree is a tree data structure in which each node has at most
# two children, referred to as the left child and the right child. For each node,
# all elements in the left subtree are less than the node, and all elements
# in the right subtree are greater than the node.

# BSTs are commonly used in databases for indexing, searching in O(log n) time,
# and maintaining a sorted list of numbers.

# =============================================================================
# Basic Node Structure
# =============================================================================
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# =============================================================================
# Basic Operations
# =============================================================================
# Insert Node
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Search Node
def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

# =============================================================================
# Tree Traversal
# =============================================================================
# In-order Traversal
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)

# =============================================================================
# Advanced Operations
# =============================================================================
# Delete Node
def delete(root, key):
    if root is None:
        return root
    
    # Find the node to be deleted
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.val = min_val(root.right)
        root.right = delete(root.right, root.val)
    return root

def min_val(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.val

# =============================================================================
# Practical Use-Cases
# =============================================================================
# - Database indexing
# - Dynamic sorting
# - Data retrieval and lookup in O(log n) time

# =============================================================================
# Testing
# =============================================================================
root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 70)
insert(root, 20)
insert(root, 40)
insert(root, 60)
insert(root, 80)

print("In-order Traversal:")
in_order_traversal(root)

# Delete node with value 20
root = delete(root, 20)
print("In-order Traversal after deletion:")
in_order_traversal(root)

# Search for node with value 60
found_node = search(root, 60)
if found_node:
    print(f"Node {found_node.val} found!")
else:
    print("Node not found.")
