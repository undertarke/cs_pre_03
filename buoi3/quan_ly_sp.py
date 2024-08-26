# maSanPham1 = input("Nhập mã sản phẩm 1: ")
# tenSanPham1 = input("Nhập mã sản phẩm 2: ")


# maSanPham2 = input("Nhập mã sản phẩm 2: ")
# tenSanPham2 = input("Nhập mã sản phẩm 2: ")


# maSanPham3 = input("Nhập mã sản phẩm 3: ")
# tenSanPham3 = input("Nhập mã sản phẩm 3: ")

# object => đối tượng
# dictionary: dics {"key":"value"} {"thuộc tính":"giá trị"}
sanPham = {
    "id": 1,
    "name": "Sản phẩm 1",
    "price": 50
}
sanPham["price"] = 100

# lấy dữ liệu từ object
# print(sanPham["tenSanPham"])

# list Object: danh sách đối tượng

danhSachSanPham = [
    {
        "maSanPham": 1,
        "tenSanPham": "Sản phẩm 1"
    },
    {
        "maSanPham": 2,
        "tenSanPham": "Macbook"
    },
    {
        "maSanPham": 3,
        "tenSanPham": "Sản phẩm 3"
    },
]
# xóa item 2, 1 dòng
danhSachSanPham = [item for item in danhSachSanPham if item["maSanPham"] != 2]

# xóa item 2
danhSachTemp = []
for item in danhSachSanPham:
    if item["maSanPham"] != 2:
        danhSachTemp.append(item)

danhSachSanPham = danhSachTemp


for item in danhSachSanPham:
    if item["maSanPham"] == 1:
        item["maSanPham"] = 1
        item["tenSanPham"] = "Macbook"

# danhSachSanPham.append(sanPham)


# duyệt => hiển thị dữ liệu
# lặp => vòng lặp (while, for)
# for each
# for ( index ; index < 10 ; index++ )

for item in danhSachSanPham:
    print(item["tenSanPham"])

danhSachSanPham.append({
    "maSanPham": 4,
    "tenSanPham": "Sản phẩm 4"
})


tenSanPham = "sản phẩm 1"
# hàm


# class: lớp đối tượng
# thuộc tính: properties
# phương thức: method
# self: con trỏ this
class SanPham:
    # hàm khởi tạo
    def __init__(self, ma, ten):
        self.maSanPham = ma
        self.tenSanPham = ten

    def nhapKho(self, a, b, c, d):
        print(self.tenSanPham)

    def xuatKho(self):
        print(self.tenSanPham, self.tenSanPham)

    def dotKho(self):
        self.nhapKho()
        self.xuatKho()
        print("")


def xuatKho(ma, ten):
    print(ma, ten)


# đối tượng
sanPham = SanPham(1, "sản phẩm 1")
sanPham.maSanPham
sanPham.tenSanPham
sanPham.xuatKho()
