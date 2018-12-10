# -*- coding: utf-8 -*
# Description
# 给定一个矩形区域，每一个位置上都是1或0，求该矩阵中每一个位置上都是1的最大子矩形区域中的1的个数。
# Input
# 输入的每一行是用空格隔开的0或1。
# Output

# Sample Input 1
# 1 0 1 1
# 1 1 1 1
# 1 1 1 0
# Sample Output 1
# 6

import sys


def max_area_histogram(histogram):
    max_area = 0
    stack = list()
    index = 0

    while index < len(histogram):
        if not stack or histogram[index] >= histogram[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            stack_top_index = stack.pop()
            current_area = histogram[stack_top_index] * (index-stack[-1]-1 if stack else index)
            max_area = max(current_area, max_area)

    while stack:
        stack_top_index = stack.pop()
        current_area = histogram[stack_top_index] * (index - stack[-1] - 1 if stack else index)
        max_area = max(current_area, max_area)

    return max_area


if __name__ == '__main__':
    # input
    data = list()
    for line in sys.stdin:
        nums = line.rstrip('\n').split(' ')
        line_data = list()
        for i in nums:
            line_data.append(int(i))
        data.append(line_data)

    # compute the histogram of the first row
    first_row_histogram = list()
    current_num = 0
    for item in data[0]:
        current_num = current_num + 1 if item == 1 else 0
        first_row_histogram.append(current_num)

    # store the histogram of the every row
    all_row_histogram = list()
    all_row_histogram.append(first_row_histogram)
    max_num = max_area_histogram(first_row_histogram)

    # continue to compute the remaining rows
    for row in data[1:]:
        this_row_histogram = list()
        for col_index in range(len(row)):
            item = row[col_index]
            if item == 0:
                this_row_histogram.append(0)
            else:
                this_row_histogram.append(all_row_histogram[-1][col_index]+1)
        all_row_histogram.append(this_row_histogram)
        max_num = max(max_num, max_area_histogram(this_row_histogram))

    print(max_num)
