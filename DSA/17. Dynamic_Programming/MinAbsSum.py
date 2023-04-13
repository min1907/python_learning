def solution(A):
    # S could be 1 or -1, it does not matter that each element in A is negative or positive
    A = [abs(item) for item in A]  # [1,5,2,2]
    sumOfA = sum(A)  # 10

    numbers = {}
    for item in A:
        numbers[item] = numbers.get(item, 0) + 1
    # numbers = {1: 1, 5: 1, 2: 2}
    # print(numbers)


A = [1, 5, 2, -2]
print(solution(A))
