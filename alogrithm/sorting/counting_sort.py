def count_sort(arr):
    max_num = max(arr)
    min_num = min(arr)

    n = max_num - min_num + 1
    count = [0 for _ in range(n)]
    for num in arr:
        count[num - min_num] += 1

    i = 0
    for j in range(n):
        while count[j] != 0:
            arr[i] = j + min_num
            count[j] -= 1
            i += 1


num = [1, 3, 2, 4, 5, 7, 6, 9, 9, 10, 8, 8]
count_sort(num)
print(num)
