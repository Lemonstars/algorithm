def heapify(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j != 0 and arr[j] > arr[(j-1) // 2]:
            arr[j], arr[(j-1) // 2] = arr[(j-1) // 2], arr[j]
            j = (j-1) // 2


array = [10, 20, 15, 17, 9, 21]
heapify(array)
print(array)
