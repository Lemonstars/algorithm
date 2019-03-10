def bucket_sort(arr):
    slot_num = 10
    bucket = [[] for _ in range(slot_num)]
    for f in arr:
        bucket[int(f*slot_num)].append(f)

    for b in bucket:
        b.sort()

    i = 0
    for b in bucket:
        for item in b:
            arr[i] = item
            i += 1


f = [0.1, 0.5, 0.4, 0.2, 0.9, 0.09, 0.03, 0.54]
bucket_sort(f)
print(f)
