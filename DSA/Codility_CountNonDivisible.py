def solution(A):
    from math import sqrt

    A_max = max(A)
    A_len = len(A)
    # Compute the frequency of occurence of each element in array A
    count = {}
    for element in A:
        count[element] = count.get(element, 0) + 1
    # {3: 2, 1: 1, 2: 1, 6: 1}

    # Compute the divisors for each element in A
    divisors = {}
    for element in A:
        # every nature number has a divisor 1
        divisors[element] = [1]
    # {3: [1], 1: [1], 2: [1], 6: [1]}

    # Use brute force to find out all divisors less than sqrt(A_max)
    # Sieve algorithm
    for divisor in range(2, int(sqrt(A_max)) + 1):
        multiple = divisor
        while multiple <= A_max:
            if (multiple in divisors) and (not divisor in divisors[multiple]):
                divisors[multiple].append(divisor)
            multiple += divisor
    # print(divisors)
    # {3: [1], 1: [1], 2: [1, 2], 6: [1, 2]}

    # In this loop, we compute all divisors greater than sqrt(A_max)
    # filter out duplicate and combine them
    for element in divisors:
        print(element)
        temp = [element // div for div in divisors[element]]
        print(temp)
        # Filter out the duplicate divisors
        temp = [item for item in temp if item not in divisors[element]]
        # print('after',temp)
        divisors[element].extend(temp)
        # print(divisors)
    # after this step we have a dictionary with element and all divisors
    # {3: [1, 3], 1: [1], 2: [1, 2], 6: [1, 2, 6, 3]}

    # The result of each number should be, the array length minus
    # the total number of occurances of its divisors
    result = []
    for element in A:
        # print([count.get(div,0) for div in divisors[element]])
        result.append(A_len - sum([count.get(div, 0) for div in divisors[element]]))
        # print(element, result)
    return result


A = [3, 1, 2, 3, 6]
# count = {3: 2, 1: 1, 2: 1, 6: 1}
# the function should return [2, 4, 3, 2, 0],
print(solution(A))
