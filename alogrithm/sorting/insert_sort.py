def insert_sort(arr):
    n = len(arr)

    for i in range(1, n):
        cur = arr[i]
        j = i - 1
        while j >= 0 and cur < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = cur


num = [5, 3, 2, 4, 1]
insert_sort(num)
print(num)
