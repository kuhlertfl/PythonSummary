# =============================================================================
# Node Class Declaration
# =============================================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# =============================================================================
# Singly Linked List with Head and Tail Class Declaration
# =============================================================================
class SinglyLinkedListWithTail:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None
        self.tail = second_last

    def add_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            return
        cur_node = self.head
        position = 0
        while cur_node and position < index - 1:
            cur_node = cur_node.next
            position += 1
        if cur_node is None:
            return
        new_node.next = cur_node.next
        cur_node.next = new_node
        if cur_node == self.tail:
            self.tail = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

# =============================================================================
# Stack Implementation Using List with Head and Tail
# =============================================================================
class Stack:
    def __init__(self):
        self.list = SinglyLinkedListWithTail()

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if self.list.head is None:
            return "Stack is empty"
        data = self.list.tail.data
        self.list.delete_last()
        return data

# =============================================================================
# Queue Implementation Using List with Head and Tail
# =============================================================================
class Queue:
    def __init__(self):
        self.list = SinglyLinkedListWithTail()

    def enqueue(self, data):
        self.list.append(data)

    def dequeue(self):
        if self.list.head is None:
            return "Queue is empty"
        data = self.list.head.data
        self.list.head = self.list.head.next
        if self.list.head is None:
            self.list.tail = None
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
