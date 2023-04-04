# Thuat toan Euclid dc su dung de tim uoc chung lon nhat cua 2 so integer duong (dung de quy - recursive)

# Thuat toan Euclid dung phep tru
def gcd1(a, b):
    if a == b:
        return a
    if a > b:
        gcd1(a - b, b)
    else:
        gcd1(a, b - a)


# Thuat toan Euclid dung phep chia
def gcd2(a, b):
    if a % b == 0:
        return b
    else:
        return gcd2(b, a % b)


# Binary Euclid algo ; call : gcd3(a,b,1)
# Su dung ki thuat Divide and Conquer
def gcd3(a, b, res):
    if a == b:
        return res * a
    elif (a % 2 == 0) and (b % 2 == 0):
        return gcd3(a // 2, b // 2, 2 * res)
    elif a % 2 == 0:
        return gcd3(a // 2, b, res)
    elif b % 2 == 0:
        return gcd3(a, b // 2, res)
    elif a > b:
        return gcd3(a - b, b, res)
    else:
        return gcd3(a, b - a, res)


print(gcd3(2, 7, 1))


# Boi chung nho nhat : least common multiple (lcm)
# lcm(a,b) = a.b/gcd(a,b)

# lcm(4,6,8) = lcm(4, lcm(6,8))
