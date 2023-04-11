def Solution(A):
    # if len(A) == 0:
    #     return 1

    setA = set(A)
    setB = set(range(1, len(A) + 2))
    Diff = setB - setA
    return list(Diff)[0]


A = [2]
print(Solution(A))
