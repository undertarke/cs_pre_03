class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False


class Trie:
    def __init__(self):
        self.root= TrieNode()

    def insert(self,word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            
        node.endWord = True

    def prirtTrie(self):
        self._prirtTrie(self.root,"")

    def _prirtTrie(self,node, current):
        if node.endWord == True:
                print(current)
        
        for char,childNode in node.children.items():
            self._prirtTrie(childNode,current+char)


products = ["cat", "banana", "obama", "batman", "car","cow", "alibaba", "cart", "catch", "on", "at"]

trie = Trie()

for item in products:
    trie.insert(item)

trie.prirtTrie()

timTu = input("Nhập từ: ")
