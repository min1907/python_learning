# from collections import Counter
def solution(A): 
    candidate = -1
    candidate_count = 0
    # candidate_index = []
    candidate_index = -1
    for index in range(len(A)):
        if candidate_count == 0:
            candidate = A[index]
            candidate_count +=1
            # candidate_index = index
        else:
            if A[index] == candidate:
                candidate_count += 1
                candidate_index = index
            else:
                candidate_count -= 1
    if len([number for number in A if number == candidate]) <= len(A)//2:
        return -1
    else:
        return candidate_index
        # for index, value in enumerate(A):
        #     if value == candidate:
        #         candidate_index.append(index)
        # return candidate_index
        

A=[3,4,3,2,3,-1,3,3]

print(solution(A))