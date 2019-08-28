def checkBST(root, min_val, max_val):
    if not root:
        return True
    if root.data > min_val or root.data < max_val:
        return False
    return checkBST(root.left, min_val, root.data-1) and checkBST(root.right, root.data+1, max_val)
  
  
