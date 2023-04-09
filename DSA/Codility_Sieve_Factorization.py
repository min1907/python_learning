# Sieve - Factorization
'''
Step 1: Tim so nguyen to nho nhat p la uoc so cua so N
Step 2: Sau khi tim dc gia tri o step 1, cac uoc so nguyen to la: p + n/p
'''

def arrayF(n): # gia tri cuoi cung cua mang tra ve la uoc so nguyen to nho nhat cua n
    F = [0] * (n+1)
    i = 2 # dai so nguyen to luon di tu 2
    while (i * i < n):
        print(i,F)
        k = i * i
        while k <= n:
            if F[k] == 0:
                F[k] = i
            k += i
        print(F)
        i += 1

    return F

def factorization(x, F):
    primeFactors = []
    while (F[x] > 0):
        primeFactors += [F[x]]
        x //= F[x]
    primeFactors += [x]
    return primeFactors

F = arrayF(35)
# print(F)
print(factorization(35,F))