class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

a = [1,2,3,4,5,6,7]

def buildTree(i):
    if i >= len(a):
        return None
    root = Node(a[i])
    root.left = buildTree(2*i+1)
    root.right = buildTree(2*i+2)
    return root

def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print(root.val)
    Inorder(root.right)

def Preorder(root):
    if not root:
        return
    print(root.val)
    Preorder(root.left)
    Preorder(root.right)

def Postorder(root):
    if not root:
        return
    Postorder(root.left)
    Postorder(root.right)
    print(root.val)

root = buildTree(0)
print('Inorder')
Inorder(root)
print('PostOrder')
Postorder(root)
print('PreOrder')
Preorder(root)
