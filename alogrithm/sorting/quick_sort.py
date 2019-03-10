def quick_sort(arr, lo, hi):
    if lo < hi:
        p = partion(arr, lo, hi)
        quick_sort(arr, lo, p-1)
        quick_sort(arr, p+1, hi)


def partion(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[hi] = arr[hi], arr[i+1]

    return i + 1


num = [4, 3, 7, 6, 1, 2, 5]
quick_sort(num, 0, len(num)-1)
print(num)