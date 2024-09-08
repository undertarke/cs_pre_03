arr = [222, 10, 1, 6, 7, 4, 2, 8, 100, 201]  # => 0 - 7

# selection sort
# i = 0 [1,10,222,6,7,4,2,8]
# i = 1 [1,2,222,6,7,4,10,8]
# i = 7


def selection_sort(arr):
    leng = len(arr)
    for i in range(leng):
        min = i
        for j in range(i+1, leng):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

# insertion sort


def insertion_sort(arr):
    leng = len(arr)
    for i in range(1, leng):
        j = i - 1
        while j >= 0:  # còn đúng là còn làm
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
            j -= 1

    return arr


arr = [222, 10, 1, 6, 7, 4, 2, 8, 100, 201]  # => 0 - 7
# [ 1, 6, 7, 4, 2, 8,10,222, 100, 201]
# [1,4,2,6,7,8] [10] [ 100,222,201]
# [1,2,4] [6] [7,8] [10] [100] [201,222]
# [1] [2] [4] .... [222]
# quick sort


def quick_sort(arr):
    leng = len(arr)
    if leng <= 1:
        return arr

    pivot = arr[1]

    left = [n for n in arr if n < pivot]
    mid = [n for n in arr if n == pivot]
    right = [n for n in arr if n > pivot]

    return quick_sort(left) + mid + quick_sort(right)

def quick_sort_n(arr):
    leng = len(arr)
    if leng <= 1:
        return arr
    
    pivot = arr[1]

    left= []
    mid=[]
    right=[]

    for n in arr:
        if n < pivot:
            left.append(n)

    for n in arr:
        if n == pivot:
            mid.append(n)

    for n in arr:
        if n > pivot:
            right.append(n)

    return quick_sort(left) + mid + quick_sort(right)

newArr = quick_sort(arr)
print(newArr)

# BigO độ phức tạp thuật toán: tính thời gian chạy lâu nhất => N 

# pip list
# macos => pip3 list