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
    root.left = reconstruct(preorder[1:root_i], inorder[0:root_i])
    root.right = reconstruct(preorder[1 + root_i:], inorder[root_i + 1:])
    return root

##cal = []
##def postorderTraversal(root):
##    global cal
##    if root:
##        postorderTraversal(root.left)
##        postorderTraversal(root.right)
##        if root.data == '+':
##            y = int(cal.pop(-1))
##            x = int(cal.pop(-1))
##            cal.append(x+y)
##        elif root.data == '-':
##            y = int(cal.pop(-1))
##            x = int(cal.pop(-1))
##            cal.append(x-y)
##        elif root.data == '*':
##            y = int(cal.pop(-1))
##            x = int(cal.pop(-1))
##            cal.append(x*y)
##        elif root.data == '/':
##            y = int(cal.pop(-1))
##            x = int(cal.pop(-1))
##            cal.append(x//y)
##        else:
##            cal.append(root.data)

##   Alternate method

def calculate(root):
    if root.data == '+':
        return int(calculate(root.left)) + int(calculate(root.right))
    elif root.data == '-':
        return int(calculate(root.left)) - int(calculate(root.right))
    elif root.data == '*':
        return int(calculate(root.left)) * int(calculate(root.right))
    elif root.data == '/':
        return int(calculate(root.left)) // int(calculate(root.right))
    else:
        return root.data
    

print("enter the preorder")
*pre_arr, = map(str, input().split())
print("enter the inorder")
*in_arr, = map(str, input().split())
high = len(pre_arr)-1
root = reconstruct(pre_arr, in_arr)
##postorderTraversal(root)
val = calculate(root)
##print(cal[0])
print(val)
