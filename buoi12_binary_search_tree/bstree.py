class Node:
    def __init__(self, product):
        self.key = product["price"]
        self.info = product
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

    def insert_node(self, product):
        self.root = self.insert(self.root, product)

    def insert(self, root, product):
        if root is None:
            return Node(product)

        if product["price"] < root.key:
            root.left = self.insert(root.left, product)
        elif product["price"] > root.key:
            root.right = self.insert(root.right, product)

        return root

    def get_tree(self, root):
        if root is None:
            return
        return {
            "key": root.key,
            "left": self.get_tree(root.left),
            "right": self.get_tree(root.right)
        }

    def find_price(self, min, max):
        result = []
        result = self.find(self.root, min, max, result)
        return result

    def find(self, root, min, max, result):
        if root is None:
            return

        if min <= root.key <= max:
            result.append(root.info)

        self.find(root.left, min, max, result)
        self.find(root.right, min, max, result)
        return result

    def find_product(self, root, price):

        if root is None:
            print("Không tìm thấy")
            return
    
        if root.key == price:
            print("Tìm thấy product trong tree")
            return
    

        if price < root.key:
            self.find_product(root.left, price)
        elif price > root.key:
            self.find_product(root.right, price)


# min - max => 2 - 5
lstProduct = [{
    "name": "product A",
    "price": 13
},
    {
    "name": "product B",
    "price": 20
},
    {
    "name": "product C",
    "price": 4
},
    {
    "name": "product D",
    "price": 2
},
    {
    "name": "product E",
    "price": 14
},
    {
    "name": "product F",
    "price": 22
},
    {
    "name": "product G",
    "price": 5
}

]
bstree = BSTree()
for product in lstProduct:
    bstree.insert_node(product)

result = bstree.find_price(2, 5)
# print(result)

# print(bstree.get_tree(bstree.root))

# nhập price từ input
# tìm ra product ở trong binary search tree

input = input("Nhập giá: ")
bstree.find_product(bstree.root,int(input))
