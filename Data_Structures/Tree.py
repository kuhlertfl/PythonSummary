# =============================================================================
# Tree Data Structure in Python
# =============================================================================

# A tree is a hierarchical data structure that consists of nodes connected by edges.
# It has a root node and each node has zero or more child nodes.

# Trees are commonly used in scenarios such as file systems, DOM, databases (B-trees, Red-Black trees),
# and routing algorithms.

# =============================================================================
# Basic Binary Tree Node
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

# =============================================================================
# Tree Traversals
# =============================================================================
# In-order Traversal
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)

# Pre-order Traversal
def pre_order_traversal(root):
    if root:
        print(root.val)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

# Post-order Traversal
def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val)

# =============================================================================
# Advanced Concepts
# =============================================================================
# Balancing a Binary Tree, Searching, Deleting Nodes are advanced topics.
# AVL Trees, Red-Black Trees, and B-Trees are types of balanced binary trees
# commonly used in databases and file systems.

# =============================================================================
# Practical Use-Cases
# =============================================================================
# - File Systems: The file directory is naturally a tree structure.
# - Routing Algorithms: OSPF, BGP use trees.
# - DOM (Document Object Model) in web browsers.
# - Priority Queues: Binary heaps are trees.
# - Databases: B-trees and variants are often used for indexing.

# =============================================================================
# Testing
# =============================================================================
# Let's create a binary search tree and add some nodes
root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 70)
insert(root, 20)
insert(root, 40)
insert(root, 60)
insert(root, 80)

# Perform in-order traversal
print("In-order Traversal:")
in_order_traversal(root)

# Perform pre-order traversal
print("Pre-order Traversal:")
pre_order_traversal(root)

# Perform post-order traversal
print("Post-order Traversal:")
post_order_traversal(root)
