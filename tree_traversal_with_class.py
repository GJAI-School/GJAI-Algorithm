class BinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left_node = left
            self.right_node = right

    def __init__(self, root=None):
        self.root = root

    def is_leaf_node(self, node):
        return node is None

    def preorder(self, node):
        if not self.is_leaf_node(node):
            print(node.data, end="")
            self.preorder(node.left_node)
            self.preorder(node.right_node)

    def inorder(self, node):
        if not self.is_leaf_node(node):
            self.inorder(node.left_node)
            print(node.data, end="")
            self.inorder(node.right_node)

    def postorder(self, node):
        if not self.is_leaf_node(node):
            self.postorder(node.left_node)
            self.postorder(node.right_node)
            print(node.data, end="")

n = int(input())
temp_dict = {}

tree = BinaryTree()

for _ in range(n):
    root, left, right = input().split()
    new_root_node = tree.Node(root)

    temp_dict[left] = {}
    temp_dict[left]['parent_node'] = new_root_node
    temp_dict[left]['order'] = 'left'

    temp_dict[right] = {}
    temp_dict[right]['parent_node'] = new_root_node
    temp_dict[right]['order'] = 'right'

    if root == 'A':
        tree.root = new_root_node
    else:
        if temp_dict[root]['order'] == 'left':
            temp_dict[root]['parent_node'].left_node = new_root_node
        else:
            temp_dict[root]['parent_node'].right_node = new_root_node
        
tree.preorder(tree.root)
print()
tree.inorder(tree.root)
print()
tree.postorder(tree.root)
print()