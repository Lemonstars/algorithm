def binary_insert_sort(arr):
    n = len(arr)

    for i in range(1, n):
        cur = arr[i]

        lo = 0
        hi = i - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if cur < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

        for k in range(i-1, lo-1, -1):
            arr[k+1] = arr[k]

        arr[lo] = cur


num = [5, 3, 2, 4, 1]
binary_insert_sort(num)
print(num)
