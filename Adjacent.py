def solve(n, arr):

    for i in xrange(0, n):

        if arr[i] % 2 == 0:
            arr[i] -= 1

    return " ".join(str(_) for _ in arr)


if __name__ == "__main__":

    n = int(raw_input())
    arr = map(int, raw_input().split(" "))
    print solve(n, arr)
