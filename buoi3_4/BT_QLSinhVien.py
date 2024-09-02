sinhVien = {
    "maSinhVien": 1,
    "tenSinhVien": "abc"
}


class SinhVien:
    def __init__(self, maSinhVien, tenSinhVien, diemToan, diemLy, diemHoa):
        self.maSinhVien = maSinhVien
        self.tenSinhVien = tenSinhVien
        self.diemToan = diemToan
        self.diemHoa = diemLy
        self.diemLy = diemHoa

    def tinhTrungBinh(self):
        return (self.diemToan+self.diemHoa+self.diemLy)/3


sinhVienMot = SinhVien(1, "sinh viên A", 1, 2, 3)
sinhVienHai = SinhVien(2, "sinh viên B", 8, 9, 10)
sinhVienBa = SinhVien(3, "sinh viên C", 5, 5, 5)

danhSachSinhVien = [sinhVienMot, sinhVienHai, sinhVienBa]

for sinhVien in danhSachSinhVien:
    diemTB = sinhVien.tinhTrungBinh()
    if diemTB >= 5:
        print(sinhVien.tenSinhVien)
    

def tinhTrungBinh(toan, ly, hoa):
    return (toan+ly+hoa)/3
