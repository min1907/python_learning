def blocksNo(A, maxBlock):
    blocksNumber = 1
    preBlockSum = A[0]
    for element in A[1:]:
        # Try to extend the previous block
        if preBlockSum + element > maxBlock:
            # Fail to extend previous block
            # because of sum limitation maxBlock
            # add new block
            preBlockSum = element
            blocksNumber += 1
            # print('here > maxBlock | ',element,preBlockSum,blocksNumber)
        else:  # preBlockSum + element <= maxBlock
            preBlockSum += element
            # print('here < maxBlock | ', element,preBlockSum)

    return blocksNumber


def solution(K, M, A):
    # A[i] <= M
    blocksNeeded = 0
    result = 0  # Minimal large sum

    resultLowerBound = max(A)
    resultUpperBound = sum(A)  # 15

    # Binary search the result
    while resultLowerBound <= resultUpperBound:
        resultMaxMid = (resultLowerBound + resultUpperBound) // 2
        blocksNeeded = blocksNo(A, resultMaxMid)
        if blocksNeeded <= K:
            resultUpperBound = resultMaxMid - 1
            result = resultMaxMid
        else:
            resultLowerBound = resultMaxMid + 1

    return result


A = [2, 1, 5, 1, 2, 2, 2]
K = 3
M = 5
print(solution(K, A))
# should return 6 sum[2,2,2]

# print(blocksNo(A,3))
