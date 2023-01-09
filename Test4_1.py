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
arr = sorted([5, 8, 9, 1, 23, 5, 7, 3, 0, 15])
number = 2
print(FindPosition(arr, number))