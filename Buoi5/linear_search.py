#         0  1  2  3  4   . . . ...
lstNum = [7, 2, 1, 9, 20, 66, 44, 84, 100, 264, 333, 631, 10, 55]


# nhập 1 số => tìm số đó trong mảng
# có trả về vị trí của số đó
# không có trả về -1

# thuật toán tím kiếm tuyến tính (linear search)
# number = int(input("Nhập số cần tìm: "))
# 9


def linear_search(number):
    index = 0
    for item in lstNum:
        if item == number:
            return index
        index += 1
    return -1

# print(linear_search(number))


# thuật toán tìm kiếm nhị phân (binary search)

def binary_seach(number):
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

# print(binary_seach(number))


# thuật toán sắp xếp bubble sort
lstNum = [7, 2, 1, 9, 20, 66, 44, 84, 100, 264, 333, 631, 10, 55]

def bubble_sort():
    leng = len(lstNum)
    for i in range(leng):
        for j in range(leng-i-1):
            if (lstNum[j] > lstNum[j+1]):
                lstNum[j], lstNum[j+1] = lstNum[j+1], lstNum[j]
                # temp = lstNum[j+1]
                # lstNum[j+1] = lstNum[j]
                # lstNum[j] = temp


bubble_sort()
print(lstNum)
