def boards(A, k):
    n = len(A)
    beg = 1
    end = n
    result = -1
    while beg <= end:
        mid = (beg + end) / 2
        if check(A, mid) <= k:
            end = mid - 1
            result = mid
        else:
            beg = mid + 1
    return result


# There is the question of how to check whether size x is sufficient. We can go through all the
# indices from the left to the right and greedily count the boards. We add a new board only if
# there is a hole that is not covered by the last board.
# Greedily check
def check(A, size):
    n = len(A)
    boards = 0
    last = -1
    for i in range(n):
        # print(A[i])
        if A[i] == 1 and last < i:
            boards += 1
            last = i + size - 1
            # print(A[i], boards, last)
    return boards


A = [1, 0, 1, 1]
# size = 3 #size of 1 board
# print(check(A, size)) # number of boards can be used to cover toan bo holes(1)

# quay tro lai bai toan ban dau
k = 3  # gia su so board ban dau la 2
print(
    boards(A, k)
)  # kich thuoc nho nhat cua 1 board de cover toan bo holes(1) voi k boards
