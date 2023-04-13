def solution(K, A):
    count = 0
    length = 0
    for rope in A:
        length += rope
        if length >= K:
            count += 1
            length = 0
    return count


A = [1, 2, 3, 4, 1, 1, 3]
K = 4
print(solution(K, A))
# should return 3 ropes [1,2,3] [4] [1,1,3]
# result: max number of ropes that have sum >= K
