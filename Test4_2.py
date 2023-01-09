def insertion(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while arr[j] > key and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr



print(insertion([-13, 6, 1, 78, 5, 34, 0, 22, -4, 121, 5]))