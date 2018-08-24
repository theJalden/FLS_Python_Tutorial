# Data Structures

# Lists = []
#   - Indexable, change values in a list
#   - Append, insert

# Tuples = ()
#   - Indexable
#   - Immutable

# Linked Lists:
# A linked is either:
#   - None
#   - Node:
#       - value
#       - next: Linked List
class Node:
    def __init__(self, val, nxt):
        self.val = val
        self.next = nxt

    def printList(self):
        print(self.val)
        self.next.printList()

    # Return the max of this node's value and the rest of
    # this list
    def maxInList(self):
        if self.next is None:
            return self.val
        else:
            return max(self.val, self.next.maxInList())

    def append(self, data):
        if self.next is None:
            self.next = Node(data, None)
        else:
            self.next.append(data)

    def length(self):
        if self.next is None:
            return 1
        else:
            return 1 + self.next.length()


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def BST_insert(self, vv):
        if vv < self.val:
            if self.left is None:
                # Create new node with vv
                self.left = TreeNode(vv)
            else:
                self.left.BST_insert(vv)
        if vv >= self.val:
            if self.right is None:
                # Create new node with vv
                self.right = TreeNode(vv)
            else:
                self.right.BST_insert(vv)

    def contains(self, num):
        if self.val == num:
            return True
        elif num < self.val:
            if self.left is None:
                return False
            else:
                return self.left.contains(num)
        elif num > self.val:
            if self.right is None:
                return False
            else:
                return self.right.contains(num)


    def printTree(self):
        if self.left is not None:
            print(self.left.printTree())
        print(self.val)
        if self.right is not None:
            print(self.right.printTree())


root = TreeNode(12)
root.BST_insert(5)
root.BST_insert(15)
root.BST_insert(1)
root.BST_insert(7)
root.BST_insert(14)
root.BST_insert(20)


print("Tree contains 7?: ", root.contains(7))
print("Tree contains 12?: ", root.contains(12))
print("Tree contains 17?: ", root.contains(17))

root.printTree()
