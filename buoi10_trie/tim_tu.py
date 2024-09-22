products = ["cat", "banana", "obama", "batman", "car",
            "cow", "alibaba", "cart", "catch", "on", "at"]

timTu = input("Nhập từ: ")
# c => cat, car, cow, cart, catch
# ca => cat, car, cart , catch
# car => car, cart

# O(n)
# for


Trie = {
    "c": {
        "o": {
            "w": {
                "endWord": True
            },
            "endWord": False
        },
        "a": {
            "t": {
                "endWord": True
            },
            "r": {
                "endWord": True
            },
            "endWord": False
        },
        "endWord": False
    },
    "o": {"b": { "a": {"m":{"a":{ "endWord": True}} }} }
}
