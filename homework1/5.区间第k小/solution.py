# Description
# 找到给定数组的给定区间内的倒数第K小的数值。
# Input
# 输入的第一行为数组，每一个数用空格隔开；第二行是区间（第几个数到第几个数，两头均包含），两个值用空格隔开；第三行为K值。
# Output
# 结果

# Sample Input 1
# 1 2 3 4 5 6 7
# 3 5
# 2
# Sample Output 1
# 4


def find_smallest_k(arr, low, high, k):
    p = partition(arr, low, high)
    num = p - low + 1
    if k > num:
        return find_smallest_k(arr, p+1, high, k-num)
    elif k < num:
        return find_smallest_k(arr, low, p-1, k)
    else:
        return arr[p]


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    j = low
    while j <= high-1:
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


# input: data, low_range, high_range, k
data = list()
for item in input().split():
    data.append(int(item))
ran = input().split()
low_range = int(ran[0])
high_range = int(ran[1])
K = int(input())

process_data = list()
index = low_range-1
while index <= high_range-1:
    process_data.append(data[index])
    index += 1

print(find_smallest_k(process_data, 0, len(process_data)-1, K))
