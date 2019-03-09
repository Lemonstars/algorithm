def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for j in range(n-1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        heapify(arr, j, 0)


def heapify(arr, n, i):
    '''
    :param arr: 数组
    :param n: 数组长度，并不一定等于len(arr)
    :param i: 最大堆的根结点下标
    :return: void
    '''

    largest = i
    left = i * 2 + 1
    right = i * 2 + 2
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


num = [6, 3, 7, 1, 4, 2, 5]
heap_sort(num)
print(num)
