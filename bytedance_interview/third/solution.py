def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)


def heap_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len - 1, -1, -1):
        heapify(arr, arr_len, i)

    for i in range(arr_len):
        arr[0], arr[arr_len - 1 - i] = arr[arr_len - 1 - i], arr[0]
        heapify(arr, arr_len - 1 - i, 0)


arr = [1, 3, 5, 4, 2, 10, 7, 8]
heap_sort(arr)
print(arr)



