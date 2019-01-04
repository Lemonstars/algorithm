# Description
# You are given N number of books. Every ith book has Pi number of pages.
# You have to allocate books to M number of students. There can be many ways or permutations to do so.
# In each permutation one of the M students will be allocated the maximum number of pages.
# Out of all these permutations, the task is to find that particular permutation in which
# the maximum number of pages allocated to a student is minimum of those in all the other permutations,
# and print this minimum value. Each book will be allocated to exactly one student.
# Each student has to be allocated at least one book.
#
# Input
# The first line contains 'T' denoting the number of test cases. Then follows description of T test cases:
# Each case begins with a single positive integer N denoting the number of books.
# The second line contains N space separated positive integers denoting the pages of each book.
# And the third line contains another integer M, denoting the number of studentsConstraints:1<= T <=70，
# 1<= N <=50，1<= A [ i ] <=250，1<= M <=50，Note: Return -1 if a valid assignment is not possible,
# and allotment should be in contiguous order (see explanation for better understanding)
#
# Output
# For each test case, output a single line containing minimum number of pages each student has to read
# for corresponding test case.

# Sample Input 1
# 1
# 4
# 12 34 67 90
# 2
#
# Sample Output 1
# 113


def is_possible(pages, num_of_stu, mid_page):
    require_stu = 1
    curr_page = 0
    for item in pages:
        if item > mid_page:
            return False

        if curr_page + item > mid_page:
            require_stu += 1
            curr_page = item
        else:
            curr_page = curr_page + item

        if require_stu > num_of_stu:
            return False

    return True


def solve(num_of_book, pages, num_of_stu):
    if num_of_book < num_of_stu:
        return -1

    sum_of_pages = sum(pages)
    start = 0
    end = sum_of_pages
    res = sum_of_pages

    while start <= end:
        mid = (start + end) // 2
        if is_possible(pages, num_of_stu, mid):
            res = min(res, mid)
            end -= 1
        else:
            start += 1

    return res


num_of_test = int(input())
while num_of_test > 0:
    n = int(input())
    data = [int(i) for i in input().split()]
    m = int(input())

    print(solve(n, data, m))

    num_of_test -= 1
