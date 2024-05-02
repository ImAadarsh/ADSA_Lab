class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_helper(self.root, val)

    def _insert_helper(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_helper(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_helper(node.right, val)

    def delete(self, val):
        self.root = self._delete_helper(self.root, val)

    def _delete_helper(self, root, val):
        if root is None:
            return root

        if val < root.val:
            root.left = self._delete_helper(root.left, val)
        elif val > root.val:
            root.right = self._delete_helper(root.right, val)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self._min_value_node(root.right)
            root.val = temp.val
            root.right = self._delete_helper(root.right, temp.val)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_helper(self.root, result)
        return result

    def _inorder_traversal_helper(self, node, result):
        if node:
            self._inorder_traversal_helper(node.left, result)
            result.append(node.val)
            self._inorder_traversal_helper(node.right, result)

# Example usage:
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)
# bst.insert(1)
# bst.insert(2)
# bst.insert(3)
# bst.insert(4)
# bst.insert(5)
# bst.insert(6)
# bst.insert(7)


print("Inorder Traversal:", bst.inorder_traversal())

bst.delete(3)
print("After deleting 3, Inorder Traversal:", bst.inorder_traversal())
