# So nguyen to la so chi co duy nhat 2 uoc so: 1 va chinh no
# De kiem tra 1 so la so nguyen to co 2 phuong phap

# Dem so luong uoc so cua 1 so (O(n))
def divisors(n):
    i = 1
    result = 0
    while i * i < n:
        if n % i == 0:
            result += 2
        i += 1
    if i * i == n:
        result += 1
    return result


# print(divisors(6)) # 4: 6 co 4 uoc so: 1,2,3,6


# Kiem tra neu 1 so la so nguyen to (O(sqrt(n)))
def primality(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# print(primality(1))

# Problem swap coin (cho n dong xu dang o vi tri ngua (Head),
# dem so dong xu o mat sap (Tail) sau khi n people lat dong xu o cac vi tri la boi so cua vi tri dang dung: vi du nguoi thu i se lat dong xu vi tri i, 2*i, 3*i,...)
# A = [0,0,0,0] -> [1,2,3,4]
# 0:H; 1:T; result:number of T
# 1: 1,1,1,1
# 2:


def Solution1(n):  # O(nlogn)
    result = 0
    coin = [0] * (n + 1)
    for i in range(1, n + 1):
        k = i
        while k <= n:
            coin[k] = (coin[k] + 1) % 2  # dao chieu dong xu o vi tri la boi so cua i
            k += i  # move k toi vi tri tiep theo la boi so cua i
        result += coin[i]  # coin[i] can be 0 or 1
    return result


# print(Solution1(9))

# cach 2: dem so lan reverse o moi vi tri(tong so cac vi tri co so lan le la ket qua can tim)
# 1 so co lan reverse le: tuong ung co so le uoc so (cac so dinh dang k^2)
def Solution2(n):  # O(logn)
    result = 0
    for i in range(1, n + 1):
        if divisors(i) % 2 == 1:
            result += 1
    return result


# print(Solution2(4))

######################################
# Sieve of Eratosthenes: ki thuat tim cac so nguyen to trong range tu 2 --> n


def sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    i = 2
    while i * i <= n:
        if sieve[i]:
            k = i * i
            while k <= n:
                sieve[k] = False
                k += i
        i += 1
    return sieve


# print(sieve(17))

#####################
# Factorization
# tim so nguyen to nho nhat(khac 1) la uoc so cua 1 so (su dung thuat toan sieve va thay doi 1 chut)


def arrayF(n):
    F = [0] * (n + 1)
    i = 2
    while i * i <= n:
        if F[i] == 0:
            k = i * i
            while k <= n:
                if F[k] == 0:
                    F[k] = i
                k += i
        i += 1
    return F


print(arrayF(20))  # 0, 0, 0, 0, 2, 0, 2, 0, 2, 3, 2, 0, 2, 0, 2, 3, 2, 0, 2, 0, 2]

# Factorization of x (O(logx))


def factorization(x, F):
    primeFactors = []
    while F[x] > 0:
        primeFactors += [F[x]]
        x //= F[x]

    primeFactors += [x]
    return primeFactors


F = arrayF(20)
print(factorization(8, F))
