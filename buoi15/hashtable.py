class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [ [] for _ in range(size) ] # 5  [ [],[],[],[],[], ] 
    
    def hashFunction(self,value):
        return value % self.size # 25%5 = 0
    
    def insert(self,value):
        index = self.hashFunction(value)
        self.table[index].append(value)
    
    def search(self,value):
        index = self.hashFunction(value)
        if  self.table[index] == -1:
            return "Không tìm thấy"
        else:
            return self.table[index]
    

lstNumber = [25,33,14,19,41,53,65,77]
# 19%5 = 4
# [25,-1,-1,33,14]

hashTable  = HashTable(len(lstNumber))
for item in lstNumber:
    hashTable.insert(item)



class HashTablePro:
    def __init__(self,size):
        self.size = size
        self.table = [ [] for _ in range(size) ] # 5  [ [],[],[],[],[], ] 
    
    def hashFunction(self,value):
        return  sum(ord(char) for char in value ) % self.size # 25%5 = 0
    
    def insert(self,value):
        index = self.hashFunction(value["category"])
        self.table[index].append(value)
    
    def search(self,value):
        index = self.hashFunction(value)
        if  self.table[index] == -1:
            return "Không tìm thấy"
        else:
            return self.table[index]
        
print(ord("h"))
print(sum(ord(char) for char in "Computer" ))   
lstProduct=[{
    "name":"Iphone",
    "category":"Phone",
    "price":4
},
{
    "name":"samsung",
    "category":"Phone",
    "price":4
},
{
    "name":"Macbook",
    "category":"Computer",
    "price":4
},
{
    "name":"MSI",
    "category":"Computer",
    "price":4
}]
hashTablePro = HashTablePro(len(lstProduct))
for item in lstProduct:
    hashTablePro.insert(item)