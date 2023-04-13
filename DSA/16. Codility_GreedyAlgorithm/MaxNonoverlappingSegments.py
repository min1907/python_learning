# def solution(A, B):
#     # No overlapping is possible.
#     if len(A) < 2:
#         return len(A)
#     count = 1       # The first segment starts a new cluster.
#     end = B[0] #5
#     index = 1       # The second segment.
#     while index < len(A):
#         print("index from 1st while loop :",index)
#         # Skip all the segments in this cluster.
#         while index < len(A) and A[index] <= end:
#             index += 1
#         # All segments are processed.
#         if index == len(A):
#             break
#         # Start a new cluster.
#         count += 1
#         end = B[index]
#     return count


def solution(A, B):
    end = -1
    cluster = 0
    size = len(B)
    if size == 0:
        return 0
    for segment in range(0, size):
        print(segment, A[segment], end, cluster)
        if A[segment] > end:  # non overlap segment, add segment to the cluster
            cluster += 1  # add new segment
            end = B[segment]
    return cluster


A = [1, 3, 7, 9, 9]
B = [5, 6, 8, 9, 10]
print(solution(A, B))
