def preorder(node, node_list):
    if node != '.':
        print(node, end="")
        preorder(node_list[node][0], node_list)
        preorder(node_list[node][1], node_list)

def inorder(node, node_list):
    if node != '.':
        inorder(node_list[node][0], node_list)
        print(node, end="")
        inorder(node_list[node][1], node_list)

def postorder(node, node_list):
    if node != '.':
        postorder(node_list[node][0], node_list)
        postorder(node_list[node][1], node_list)
        print(node, end="")

n = int(input())
node_list = {}

for _ in range(n):
    root, left, right = input().split()
    node_list[root] = [left, right]

preorder('A', node_list)
print()

inorder('A', node_list)
print()

postorder('A', node_list)
print()