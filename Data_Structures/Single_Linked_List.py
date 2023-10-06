# =============================================================================
# Node Class Declaration
# =============================================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# =============================================================================
# Singly Linked List Class Declaration
# =============================================================================
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Add node to the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    # Delete the last node from the list
    def delete_last(self):
        if self.head is None:
            print("The list is empty.")
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    # Add node at a specific index
    def add_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        cur_node = self.head
        position = 0
        while cur_node and position < index - 1:
            cur_node = cur_node.next
            position += 1
        if cur_node is None:
            print("Index out of bounds")
            return
        new_node.next = cur_node.next
        cur_node.next = new_node

    # Print linked list
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

# =============================================================================
# Extended Usage Example
# =============================================================================
# Initializing a new singly linked list and performing operations.
sll = SinglyLinkedList()
sll.append("A")
sll.append("B")
sll.append("C")
print("Original List:")
sll.print_list()

sll.delete_last()
print("After Deleting Last Node:")
sll.print_list()

sll.add_at_index(1, "D")
print("After Adding at Index 1:")
sll.print_list()

# Output will be:
# Original List:
# A
# B
# C
# After Deleting Last Node:
# A
# B
# After Adding at Index 1:
# A
# D
# B

# =============================================================================
# Additional Explanations
# =============================================================================
# 1. `delete_last()`: This method deletes the last node in the list.
#    - If the list is empty, it prints a message and returns.
#    - If the list has only one node, it sets `head` to `None`.
#    - Otherwise, it traverses to the second last node and sets its `next` to `None`.

# 2. `add_at_index(index, data)`: This method adds a new node with the given data at a specific index.
#    - If the index is 0, it adds the node at the beginning.
#    - It traverses the list to the `(index - 1)`th node and inserts the new node after it.
#    - If the index is out of bounds, it prints a message and returns.

# =============================================================================
# Stack Implementation Using Singly Linked List
# =============================================================================
class Stack:
    def __init__(self):
        self.list = SinglyLinkedList()

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if self.list.head is None:
            return "Stack is empty"
        data = self.list.head.data
        self.list.delete_last()
        return data

# =============================================================================
# Queue Implementation Using Singly Linked List
# =============================================================================
class Queue:
    def __init__(self):
        self.list = SinglyLinkedList()

    def enqueue(self, data):
        self.list.append(data)

    def dequeue(self):
        if self.list.head is None:
            return "Queue is empty"
        data = self.list.head.data
        self.list.head = self.list.head.next
        return data

# =============================================================================
# Testing Stack and Queue
# =============================================================================
# Initialize a stack and push some elements
s = Stack()
s.push("A")
s.push("B")
s.push("C")
print("Popped from Stack:", s.pop())  # Should print C

# Initialize a queue and enqueue some elements
q = Queue()
q.enqueue("X")
q.enqueue("Y")
q.enqueue("Z")
print("Dequeued from Queue:", q.dequeue())  # Should print X