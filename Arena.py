def solve(n, arr):
    min_elem = min(arr)

    min_elem_freq = 0
    for a in arr:
        if a == min_elem:
            min_elem_freq += 1

    return n - min_elem_freq


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        n = int(raw_input())
        arr = map(int, raw_input().split(" "))
        print solve(n, arr)
