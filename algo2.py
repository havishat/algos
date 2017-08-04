import math

def algo2(m,f):
    count = 0
    while m != 1 or f != 1:
        if m < 1 or f < 1 or (m%2 == 0 and f%2 == 0):
            return "Impossible"
        elif m == 1:
            count += f - 1
            f = 1
        elif f == 1:
            count += m - 1
            m = 1
        elif m > f:
            count += math.floor(m / f);
            m = m % f
        elif f > m:
            count += math.floor(f / m);
            f = f % m
    return count
