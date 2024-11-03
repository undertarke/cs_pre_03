class Graph:
    def __init__(self):
        self.graph = {}

    def ketBan(self, vertex1, vertex2):

        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

        # dùng cho đồ thị vô hướng
        if vertex2 in self.graph:
            self.graph[vertex2].append(vertex1)
        else:
            self.graph[vertex2] = [vertex1]

    def layBanBe(self, vertex):
        return self.graph[vertex]


listUser = [{
    "id": 1,
    "ten": "Bạn"
},
    {
    "id": 2,
    "ten": "Bạn A"
},
    {
    "id": 3,
    "ten": "Bạn B"
},
    {
    "id": 4,
    "ten": "Bạn Z"
}, {
    "id": 5,
    "ten": "Người D"
}, {
    "id": 6,
    "ten": "Người E"
}, {
    "id": 7,
    "ten": "Người C"
}, {
    "id": 8,
    "ten": "Người Y"
}, {
    "id": 9,
    "ten": "Người T"
}
]

graph = Graph()

graph.ketBan(1, 2)
graph.ketBan(1, 3)
graph.ketBan(1, 4)

graph.ketBan(2, 5)
graph.ketBan(2, 6)

graph.ketBan(5, 8)

graph.ketBan(3, 7)

graph.ketBan(7, 9)

# print(graph.graph)

timBan = input("nhap ma nguoi de xuat: ")

# print(graph.layBanBe(int(timBan)))

lstSuggest = set()

for item in graph.layBanBe(int(timBan)):
    lstFriend = graph.layBanBe(item)
    lstSuggest.update(lstFriend)

lstSuggest.discard(int(timBan))

print(lstSuggest)

print("Gợi ý bạn bè: ")
for item in lstSuggest:

    for user in listUser:
        if user["id"] == item:
            print(user["ten"])
