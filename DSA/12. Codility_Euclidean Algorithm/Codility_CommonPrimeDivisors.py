# Tim uoc chung lon nhat
def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


# print(gcd(75,15))


def removeCommonDivisors(x, y):
    """
    Remove all common prime Divisors (greatest common divisor composed by these common prime divisors)
    of x and y and return remaining of x
    """
    while x != 1:
        gcd_value = gcd(x, y)
        if gcd_value == 1:
            break
        else:
            x //= gcd_value
    return x


# print(removeCommonDivisors(75,12))


def hasSamePrimeDivisors(x, y):
    """
    if x and y has exactly same common prime divisors.
    after removing from removeCommonDivisors,
    the remaining value are same and equal to 1
    """
    gcd_value = gcd(x, y)
    x = removeCommonDivisors(x, y)
    if x != 1:
        return False
    else:  # x == 1
        y = removeCommonDivisors(y, gcd_value)
        if y == 1:
            return y


def solution(A, B):
    result = 0
    len_A = len(A)
    for index in range(len_A):
        if hasSamePrimeDivisors(A[index], B[index]) == 1:
            result += 1
    return result


A = [1]
B = [1]
print(solution(A, B))


# def solution(A,B):
#     result = 0
#     len_A = len(A)
#     for index in range(len_A):
#         if check(A[index], B[index]) == True:
#             result += 1
#     return result

# def check(N,M):
#     # Kiem tra xem cap N,M co cung prime divisors khong
#     if M > N:
#         if M % N == 0:
#             if N % (M // N) == 0:
#                 return True
#     elif M < N:
#         if N % M == 0:
#             if M % (N // M) == 0:
#                 return True
