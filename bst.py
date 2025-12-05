class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.tree = None

    def insert(self, key, value):
        self.tree = self._insert_recursive(self.tree, key, value)

    def _insert_recursive(self, node, key, value):
        if node is None:
            return TreeNode(key, value)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key, value)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, value)
        else:
            node.value = value
        return node

    def search(self, key):
        return self._search_recursive(self.tree, key)
    
    def _search_recursive(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self._search_recursive(node.left, key)
        if key > node.key:
            return self._search_recursive(node.right, key)    
        return node.value
        
    def delete(self, key): 
        self.tree = self._delete_recursive(self.tree, key)
    
    def _delete_recursive(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        if key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            successor = self._get_min_node(node.right)
            node.key = successor.key
            node.value = successor.value
            node.right = self._delete_recursive(node.right, successor.key)
        return node
            
    def _get_min_node(self, node):
        while node.left is not None:
            node = node.left
        return node
        
    def height(self):
        return self._height_recursive(self.tree)

    def _height_recursive(self, node):
        if node is None:
            return -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1

    def is_balanced(self):
        return self._is_balanced_recursive(self.tree) != -1

    def _is_balanced_recursive(self, node):
        if node is None:
            return 0

        left_height = self._is_balanced_recursive(node.left)
        if left_height == -1:
            return -1

        right_height = self._is_balanced_recursive(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1


tree = BinarySearchTree()

tree.insert(10, 10)
tree.insert(12, 12)
tree.insert(11, 11)
tree.insert(9, 9)
tree.insert(8, 8)

print(tree.height())
print(tree.search(8))
print(tree.search(100))
print(tree.is_balanced())
tree.delete(12)
print(tree.height())
print(tree.search(11))