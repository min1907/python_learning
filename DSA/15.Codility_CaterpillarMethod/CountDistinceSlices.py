# Brute force - bad algorithm O(N**3) --> 50%
def solution(M, A):
    n = len(A)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if check_distinct(A, i, j) == True:
                count += 1
    return min(count, 1000000000)


def check_distinct(A, i, j):
    if len(A[i : j + 1]) == len(set(A[i : j + 1])):
        return True
    return False


# A = [3,4,5,5,2]
# print(solution(5,A))
# print(check_distinct(A,0,0))

# Caterpillar Algorithm
def check_distinct(A, i, j):
    if len(A[i : j + 1]) == len(set(A[i : j + 1])):
        return True
    return False


def solution2(M, A):  # 70% O(N*(N+M))
    count = 0
    N = len(A)
    index_front = 0

    for index_back in range(N):
        # print("+++++++++++++++++++++++++++++++++++")
        # print(f"back = {index_back}")
        # print("Start while loop for index_front")
        index_front = index_back
        while index_front < N and check_distinct(A, index_back, index_front) == True:
            # print ("Continue while loop ; next index_front")
            # print(f"front = {index_front}")
            index_front += 1
            count += 1
            # print(f"count = {count}")

        # print("next index_back \n")
    return min(count, 1000000000)


A = [3, 4, 5, 5, 2]
print(solution2(5, A))
