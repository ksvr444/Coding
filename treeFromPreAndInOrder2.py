class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def reconstruct(preorder, inorder):
    if not preorder and not inorder:
        return None
    if len(preorder) == len(inorder) == 1:
        return Node(preorder[0])

    root = Node(preorder[0])
    root_i = inorder.index(preorder[0])
    root.left = reconstruct(preorder[1:1 + root_i], inorder[0:root_i])
    root.right = reconstruct(preorder[1 + root_i:], inorder[root_i + 1:])
    return root


def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.data, end = " ")
        inorderTraversal(root.right)


print("enter the preorder")
*pre_arr, = map(str, input().split())
print("enter the inorder")
*in_arr, = map(str, input().split())
high = len(pre_arr)-1
root = reconstruct(pre_arr, in_arr)
inorderTraversal(root)
