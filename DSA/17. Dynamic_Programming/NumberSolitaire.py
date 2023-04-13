# key point: because of 6-sided die, we can only come to position i+1,i+2,...,i+6
# or in another word: to achieve a position, we can only come from positions i-6, i-5, i-4, i-3, i-2, i-1
def solution(A):
    N = len(A)
    # The first six items are used for padding only, so that we can have
    # a unified for loop, no matter how many squares are there in input.
    # The first item is never accessed.
    max_so_far = [A[0]] * (N + 6)  # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # print(max_so_far)
    for index in range(
        1, N
    ):  # need to calculate sum(A[0] + ... + A[N-1]) so we can start at A[1]
        # Because we have a fixed length of window as 6, the time
        # complexity of max(max_so_far[index : index + 6]) is O(1)
        max_so_far[index + 6] = max(max_so_far[index : index + 6]) + A[index]
        print(index, index + 6, max_so_far)
    return max_so_far[-1]


A = [1, -2, 0, 9, -1, -2]  # len(A) = N = 6
print(solution(A))
# should return 8 because it's the maximum sum
# index[0,3,5] = 1 + 9 +(-2) = 8

# A[0] + max + A[N-1]
# 2<=N<=100000
# -10000<=A[i] <=10000
