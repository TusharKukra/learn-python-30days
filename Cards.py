def solve(n, jumbled):

    result = list()

    for i in xrange(0, n):
        if jumbled[i] == 'z':
            result.append('0') # append
        elif jumbled[i] == 'n':
            result.insert(0, '1') # prepend

    return " ".join(result)


if __name__ == "__main__":

    n = int(raw_input())
    jumbled = raw_input()
    print solve(n, jumbled)
