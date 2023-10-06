# =============================================================================
# Binary Tree in Python
# =============================================================================

# A Binary Tree is a tree data structure in which each node has at most two children,
# commonly referred to as the "left" and "right" children.

# Binary Trees are used in various applications ranging from simple algorithms to complex
# computer programs like parsers and databases.

# =============================================================================
# Basic Node Structure
# =============================================================================
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# =============================================================================
# Insertion Operation
# =============================================================================
# The insertion in a Binary Tree generally occurs level by level,
# from top to bottom and from left to right.
# We use a queue to keep track of the nodes in level-order.
# We insert the new node at the first empty spot (either a left or right child).

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        queue = []
        queue.append(root)

        while queue:
            temp = queue.pop(0)
            
            if not temp.left:
                temp.left = Node(key)
                break
            else:
                queue.append(temp.left)

            if not temp.right:
                temp.right = Node(key)
                break
            else:
                queue.append(temp.right)

    return root


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
# Practical Use-Cases
# =============================================================================
# - Parsing expressions
# - Huffman encoding trees
# - As a workflow for compositing digital images for visual effects

# =============================================================================
# Testing
# =============================================================================
root = None
root = insert(root, 1)
insert(root, 2)
insert(root, 3)
insert(root, 4)
insert(root, 5)

print("In-order Traversal:")
in_order_traversal(root)
