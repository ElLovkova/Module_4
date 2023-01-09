def FindPosition(arr, number):
    first = 0
    last = len(arr) - 1
    while first <= last:
        middle = first + (last - first) // 2
        if arr[middle] == number:
            return middle
        elif arr[middle] < number:
            first = middle + 1
        else:
            last = middle - 1
    return -1
arr = sorted([5, 6, 9, 1, 23, 5, 11, 4, 0, 16])
#number = 2
number = 9
print(FindPosition(arr, number))