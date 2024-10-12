class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
        self.height = 1


def getHeight(node):

    if not node:
        return 0

    return node.height


def updateHeight(node):
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))


def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)  # 0 1 2 , 0 -1 -2


def insert(root, value):
    if not root:
        return Node(value)

    if root.key < value:
        root.right = insert(root.right, value)
    elif root.key > value:
        root.left = insert(root.left, value)
    

    updateHeight(root)

    # [-1 , 0 , 1]: balance
    # [-2 , 2] : not balance

    # lệch trái => quay phải
    if (getBalance(root) > 1 and value < root.left.key):
        print(f"lệch trái khi thêm :{value}")
        return rightRotate(root)

    # lệch trái-phải =>  quay trái - phải
    if (getBalance(root) > 1 and value > root.left.key):
        print(f"lệch trái-phải khi thêm :{value}")
        root.left = leftRotate(root.left)
        return rightRotate(root)

    # lệch phải =>  quay trái
    if (getBalance(root) < -1 and value > root.right.key):
        print(f"lệch phải khi thêm :{value}")
        return leftRotate(root)
    
    # lệch phải-trái =>  quay phải-trái
    if (getBalance(root) < -1 and value < root.right.key):
        print(f"lệch phải-trái khi thêm :{value}")
        root.right = rightRotate(root.right)
        return leftRotate(root)
    
    return root

def rightRotate(treeNotBalance):
    leftChild = treeNotBalance.left
    subTree = leftChild.right

    treeNotBalance.left = subTree
    leftChild.right = treeNotBalance

    updateHeight(treeNotBalance)
    updateHeight(leftChild)

    return leftChild


def leftRotate(treeNotBalance):
    rightChild = treeNotBalance.right
    subTree = rightChild.left

    treeNotBalance.right = subTree
    rightChild.left = treeNotBalance

    updateHeight(treeNotBalance)
    updateHeight(rightChild)

    return rightChild


lstChar = ["A", "B", "C", "D", "E", "F", "W", "Z", "U", "T", "K"]
lstNumber =[10,7, 2, 1,84,100, 9, 20, 66, 44, 55,3]


avlTree = None 
for item in lstChar:
    avlTree = insert(avlTree,item)

def duyet_tree(root):
    if root is None:
        return None
    return {
        'key':root.key,
        'left':duyet_tree(root.left),
        'right':duyet_tree(root.right)
    }

print(duyet_tree(avlTree))