# prefix sum is defined as consecutive totals of first 0,1,2,...,n elements of array
def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


# P = [0, 2, 5, 12, 17, 18, 21, 30]

# count total (or suffix sum) will calculate sum of all elements from postion x and postion y
def count_total(P, x, y):
    return P[y + 1] - P[x]


A = [2, 3, 7, 5, 1, 3, 9]
P = prefix_sums(A)
print(count_total(P, 2, 5))  # 16 = 7+5+1+3 = 21-5
