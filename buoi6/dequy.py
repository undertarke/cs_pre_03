

def dequy(n):
    if n == 0:
        return 0
    print(n)
    return dequy(n-1)


# khi nào mới xài đệ quy => cha , con và không điểm dừng

# Bài 1: Tính giai thừa của số nguyên: 4! = 1*2*3*4 => 24 , 5! = 1*2*3*4*5 = 120
def tinhGiaiThua(n):  # 4 3 2 1
    if n == 0:
        return 1

    return n*tinhGiaiThua(n-1)




# Bài 2: Tính tổng các chữ số của một số nguyên: 2+3 => 5, 6+2+1 = 9 , 1+1+1+1 = 4


def tinhTong(n):  # 12 3 4 = 10
    if n == 0:
        return 0
    return n % 10 + tinhTong(n//10)


# Bài 3: Đảo ngược chuỗi => Hello => olleH , 1234 => 4321
# Bài 4: Tìm số lớn nhất trong mảng => [1,2,3,4,5,6] => 6


# Tìm kiếm nhị phân
def binary_seach(number, lstNum):
    start = 0
    end = len(lstNum) - 1
    while start <= end:
        mid = int((start + end) / 2)  # 6

        if lstNum[mid] == number:
            return mid
        elif number > lstNum[mid]:
            # qua phải
            start = mid + 1
        else:
            # qua trái
            end = mid - 1

    return -1





# mid = 4 => 3

#  [1,2,3,4,5,6,7,8,9]
#  => 10


def binary_seach_dequy(number, lstNum,start,end):
    
    if start > end:
        return -1
    
    mid = (start+end)//2

    if lstNum[mid] == number:
        return mid
    elif number > lstNum[mid]:
        return binary_seach_dequy(number,lstNum,mid+1,end)
    else:
        return binary_seach_dequy(number,lstNum,start,mid-1)

print(binary_seach_dequy(10,[1,2,3,4,5,6,7,8,9],0,8))