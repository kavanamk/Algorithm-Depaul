#Kavana Manvi Krishnamurthy 
#Depaul ID = 2158984
import math
import sys

def splitmultiply(x, y):
    n = math.ceil(max(math.log2(max(1, x)), math.log2(max(1, y))))
    if n <= 2:
        return x * y
    else:
        m = n // 2
        a = x >> m
        b = x - (a << m)
        c = y >> m
        d = y - (c << m)
        e = splitmultiply(a, c)
        f = splitmultiply(b, d)
        g = splitmultiply(b, c)
        h = splitmultiply(a, d)
        return (e << (2 * m)) + ((g + h) << m) + f

if __name__ == "__main__":
    print("Kavana Manvi Krishnamurthy")
    if len(sys.argv) != 3:
        print("Usage: python splitmultiply.py x y")
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        result = splitmultiply(x, y)
        print(result)



