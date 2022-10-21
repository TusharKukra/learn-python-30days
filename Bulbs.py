def solve(bulbs):

    for bulb in bulbs:
        if bulb is 0:
            return "NO"

    return "YES"

if __name__ == "__main__":
    n,m = map(int, raw_input().split(" "))

    bulbs = [0] * m #array sized for m bulbs
    for _n in xrange(0, n):
        vals = map(int, raw_input().split(" "))
        vals.pop(0) 
        for bulbIdx in vals:
            bulbs[bulbIdx-1] = 1 

    print solve(bulbs)
