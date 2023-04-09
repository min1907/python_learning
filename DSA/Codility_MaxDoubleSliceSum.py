'''
A variant of the classic maximum subarray problem. We should travel the array twice. 
For the first travel, we compute and record the maximum sub-array sum, which ends at each position. 
At the second reverse travel, we compute and record the maximum sub-array sum, which starts at each position. 
Finally, we combine two sub-arrays into one double slice, and find out the maximum sum.
'''
'''
Update on 2016/12/12: as VuThanhCong pointed out in the comment, 
the range to compute max_ending_here and max_beginning_here could be smaller by one element: 
max_ending_here should be calculated from value in range(1, N-2); 
max_beginning_here should be calculated from value in range(N-2, 1, -1).

index(arrayA) = [0,1,...,N-1] 
min(X+1) = 0+1 = 1 (start from position 1 for head subarray)
max(Z-1) = N-1 - 1 = N-2 (end at position N-2 for tail subarray)

'''
'''
https://en.wikipedia.org/wiki/Maximum_subarray_problem
'''
# this problem requirement does not mention about result can be negative value, empty array are admitted
def solution(A):
    len_A = len(A) # len of array A
    # Get the sum of maximum subarray, which ends this position
    max_ending_here = [0] * len_A
    max_ending_here_temp = 0
    for index in range(1, len_A - 2):
        max_ending_here_temp = max(0, max_ending_here_temp + A[index])
        max_ending_here[index] = max_ending_here_temp
    
    # Get the sum of maximum subarray, which begins this position
    # same method, but we travel from the tail to head
    max_begining_here = [0] * len_A
    max_begining_here_temp = 0
    for index in range(len_A - 2, 1, -1):
        max_begining_here_temp = max(0, max_begining_here_temp + A[index])
        max_begining_here[index] = max_begining_here_temp

    '''
    Connect 2 subarrays if first sub array ends at position i, and 2nd sub array starts at position i+2
    Then we compare each double slice to get the one which has greatest sum
    '''
    max_double_slice = 0
    for index in range(0, len_A - 2): #it will return 0 incase all pairs return 0 or negative
        max_double_slice = max(max_double_slice, max_ending_here[index] + max_begining_here[index + 2])
    return max_double_slice



A=[3,2,6,-1,4,5,-1,2]
print(solution(A))