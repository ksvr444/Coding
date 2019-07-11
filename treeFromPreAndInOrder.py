class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def treeFromPreAndInOrder(pre_arr, in_arr, low, high, pre_ind):
    if pre_ind > high:
        return None
    data = pre_arr[pre_ind]
    nn = Node(data)
    
    if low == high:
        return nn
    root_ind = in_arr.index(data)
    nn.left = treeFromPreAndInOrder(pre_arr, in_arr, low, root_ind - 1, pre_ind + 1)
    nn.right = treeFromPreAndInOrder(pre_arr, in_arr, root_ind + 1, high, root_ind+1)
    return nn
    

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
root = treeFromPreAndInOrder(pre_arr, in_arr, 0, high, 0)
inorderTraversal(root)
