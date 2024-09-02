

class NhanVien:
    def __init__(self, maNhanVien, tenNhanVien, chucVu, luong, heSo):
        self.maNhanVien = maNhanVien
        self.tenNhanVien = tenNhanVien
        self.luong = luong
        self.chucVu = chucVu
        self.heSo = heSo

    def tinhLuong(self):
        # 1
        # 2
        # 4
        return self.luong*self.heSo

# quan ly phong ban có bonus


class QuanLy(NhanVien):
    def __init__(self, maNhanVien, tenNhanVien, luong, chucVu, heSo, bonus):
        super().__init__(maNhanVien, tenNhanVien, luong, chucVu, heSo)
        self.bonus = bonus

    def tinhLuong(self):
        return super().tinhLuong() + self.bonus

# quan ly chi nhanh, ko bonus


class GiamDoc(NhanVien):
    def __init__(self, maNhanVien, tenNhanVien, luong, chucVu, heSo):
        super().__init__(maNhanVien, tenNhanVien, luong, chucVu, heSo)


giamDoc = GiamDoc(1, "giám 1",  "GD", 5, 10)

# print(giamDoc.tinhLuong())

# OOP: 4 tính chất
# - tính kế thừa
# - tính đóng gói
# - tính đa hình
# - tính trừu tượng

lst = [6,3,2,8,0,4,3,7,22,29,23]

lst.sort()

print(lst)