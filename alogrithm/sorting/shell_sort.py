def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            cur = arr[i]
            j = i
            while j >= gap and cur < arr[j-gap]:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = cur

        gap //= 2


num = [5, 3, 2, 4, 1]
shell_sort(num)
print(num)
