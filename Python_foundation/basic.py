# # Print the name in list that has 6 characters length
# names = ["Jerry", "Kramer", "Elaine", "George", "Newman"]
# # Print the list created by using list comprehension
# best_list = [name for name in names if len(name) >= 6]
# print(best_list)

# Reversing an array

# def reverse(A):
#     N = len(A)
#     for i in range(N//2):
#         k = N-i-1
#         A[i],A[k] = A[k],A[i]
#     return A

# B = [1, 3, 1, 4, 2, 3, 4, 4, 5]
# print(reverse(B))

# def quadratic(n):
#     result = 0
#     for i in range(n):

#         for j in range(i, n):
#             print("i = ",i)
#             print("j = ",j)
#             result += 1
#             print("result = ", result)
#     return result

# print(quadratic(3))


# Ham dem so phan tu xuat hien trong 1 mang va luu ket qua trong mang count
def counting(A, m):
    n = len(A)
    count = [0] * (m + 1)
    for k in range(n):
        count[A[k]] += 1
    return count


def solution(A, B, m):
    n = len(A)
    sumA = sum(A)
    sumB = sum(B)
    d = sumB - sumA
    print(f"difference d between 2 arrays : {d}")
    if d % 2 == 1:
        return False

    d //= 2
    count = counting(A, m)

    for i in range(n):
        if 0 <= B[i] - d and B[i] - d <= m and count[B[i] - d] > 0:
            print(f"B[i] = {B[i]}; A[i] = {B[i]-d}")
            return True
    return False


array1 = [1, 2, 1, 3, 4, 3, 7]
# count = counting(A,7) = [0, 2, 1, 2, 1, 0, 0, 1]
array2 = [2, 1, 5, 6, 2, 0, 9]
m = 7
# d = 25-21 = 4 -> d = d//2 = 2
# B[i] - d = [0, -1, 3, 4, 0, -2, 7]
# count[B[i] - d] = [0, ]
print(solution(array1, array2, m))
