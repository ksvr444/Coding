def checkBST(root):
  if root.left != None and root.right != None:
    if not root.left.data < root.data < root.right.data:
      return False
  elif root.left == None and root.right != None:
    if not root.data < root.right.data:
      return False
  elif root.left != None and root.right == None:
    if not root.left.data < root.data:
      return False
  else:
    return True
  return checkBST(root.left) and checkBST(root.right)
