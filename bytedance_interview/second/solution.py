# coding=utf-8
import sys


def partion(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[hi], arr[i + 1] = arr[i + 1], arr[hi]
    return i + 1


def find_mid(arr):
    arr_len = len(arr)
    mid = arr_len // 2

    lo = 0
    hi = arr_len - 1
    while True:
        this_index = partion(arr, lo, hi)
        if this_index == mid:
            return arr[this_index]
        else:
            if this_index < mid:
                lo = this_index + 1
            else:
                hi = this_index - 1


print(find_mid([1, 4, 5, 2, 3]))