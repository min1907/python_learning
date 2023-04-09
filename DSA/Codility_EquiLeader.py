def solution(A):
    candidate = -1
    candidate_count = 0
    #candidate_index = -1
    for index in range(len(A)):
        if candidate_count == 0:
            candidate = A[index]
            candidate_count +=1
            # candidate_index = index
        else:
            if A[index] == candidate:
                candidate_count += 1
                #candidate_index = index
            else:
                candidate_count -= 1
    leader_count = len([number for number in A if number == candidate]) 
    if leader_count <= len(A)//2:
        # Candidate is not leader
        return 0
    else:
        leader = candidate
    equi_leaders = 0
    leader_count_so_far = 0
    for index in range(len(A)):
        if A[index] == leader:
            leader_count_so_far += 1
        if leader_count_so_far > (index + 1)//2 and (leader_count - leader_count_so_far) > (len(A) - index - 1)//2:
            # Both head and tail have leaders of the same value
            equi_leaders += 1
    return equi_leaders

A=[4,3,4,4,4,2]
print(solution(A))