def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


num = [5, 3, 2, 4, 1]
bubble_sort(num)
print(num)
