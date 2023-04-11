"""
Let the length of one side be len_1, and the length of one adjacent side be len_2.
For a rectangle with a constant area, the perimeter is minimized when the difference between len_1 and len_2, abs(len_1- len_2), is minimized.
Bai toan quy ve tim uoc so nguyen to lon nhat cua 1 so : complexity O(sqrt(N))

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.

result = 22

"""


def solution(N):
    from math import sqrt

    # result = float('inf')
    for i in range(int(sqrt(N)), 0, -1):
        if N % i == 0:
            return 2 * (i + N // i)


print(solution(30))

# from math import sqrt
# print(int(sqrt(30)))
