def maxslice(A):
    max_ending = max_slice = 0
    for a in A:
        print(f"a={a},max_ending_previous={max_ending}")
        max_ending = max(0, max_ending + a)
        print(f"a={a},max_ending_after={max_ending}")
        print(f"a={a},max_slice_previous={max_slice}")
        max_slice = max(max_slice, max_ending)
        print(f"a={a},max_slice_after={max_slice}")
        print("-------------------")

    return max_slice


A = [5, -7, 3, 5, -2, 4, -1]
print(maxslice(A))
