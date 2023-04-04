# Find a subsequence whose total of elements equal s
def CaterpillarMethod(A, s):
    n = len(A)
    front = 0
    total = 0
    for back in range(n):
        while front < n and total + A[front] <= s:
            total += A[front]
            front += 1
        if total == s:
            # return A[back:front]
            return True
        total -= A[back]
    return False


# A = [6, 2, 7, 4, 1, 3, 6]
# print(CaterpillarMethod(A, 14))

# Exercise:
# Have n sticks, count number of triangles can be constructed using these sticks (count number of triples at indices x<y<z such that ax + ay > az)
# Number of triangles


def triangles(A):
    n = len(A)
    result = 0
    for x in range(n):
        z = x + 2
        for y in range(x + 1, n):
            while z < n and A[x] + A[y] > A[z]:
                z += 1
            result += z - y - 1
    return result


A = [1, 2, 3, 4, 5, 6, 7]
print(triangles(A))
