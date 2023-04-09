'''
Write an efficient algorithm for the following assumptions:

. N is an integer within the range [1..1,000,000];
. each element of array A is an integer within the range [−1,000,000..1,000,000];
. the result will be an integer within the range [−2,147,483,648..2,147,483,647].
--> note 3: result can be negative value, so max_ending = max(a, max_ending + a)

for empty subarray are admitted, result will return 0 if input contains no positive elements (including when the input is empty) 

'''
# cho moi vi tri, ta se tinh toan largest sum ending tai vi tri do. 
# Gia su maximum sum ending tai vi tri i la max_ending
# khi do maximal slice ending o vi tri i+1 se la max(A[i+1], max_ending + A[i+1])
def solution(A):
    N = len(A)
    max_ending = max_slice = A[0]
    for a in A[1:N]:
        print(f"a={a},max_ending_previous={max_ending}")
        max_ending = max(a, max_ending + a)
        print(f"a={a},max_ending_after={max_ending}")
        print(f"a={a},max_slice_previous={max_slice}")
        max_slice = max(max_slice, max_ending)
        print(f"a={a},max_slice_after={max_slice}")
        print("-------------------")
    return max_slice

A = [3,2,-6,4,0]
print(solution(A))