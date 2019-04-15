import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    h = list(map(int, line.split()))
    max_h = max(h)

    lo = min(h)
    hi = max_h
    res = max_h
    while lo <= hi:
        mi = (lo + hi) // 2
        e = mi
        success = True
        for item in h:
            if e > item:
                e += (e - item)
            else:
                e -= (item - e)

            if e < 0:
                success = False
                break

        if success:
            if mi < res:
                res = mi
            hi = mi - 1
        else:
            lo = mi + 1

    print(res)