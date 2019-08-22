import queue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def createTree():
    x = int(input())
    if x == -1:
        return
    temp = Node(x)
    temp.left = createTree()
    temp.right = createTree()
    return temp

def inorder(root):
    if(root):
        inorder(root.left)
        print(root.data)
        inorder(root.right)

# def levelWisePrint(root):
#     arr = []
#     arr.append(root)
#     while arr:
#         temp = arr.pop(0)
#         if temp:
#             print(temp.data)
#             arr.append(temp.left)
#             arr.append(temp.right)

def levelWisePrint(root):
    que = queue.Queue()
    que.put(root)
    while not que.empty():
        temp = que.get()
        print(temp.data)
        if temp.left :
            que.put(temp.left)
        if temp.right:
            que.put(temp.right)

root = createTree()
inorder(root)
print("level")
levelWisePrint(root)
