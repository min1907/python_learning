# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    # Implement your solution here
    # Calculate the sum
    sum = 0
    for i in range(len(S)):
        sum += int(S[i])

    # Store the answer
    count = 0
    if sum % 3 == 0:
        count += 1

    # Iterate over the range
    for i in range(len(S)):

        # Decreasing the sum
        remaining_sum = sum - int(S[i])

        # Iterate over the range
        for j in range(10):

            # Checking if the new sum
            # is divisible by 3 or not
            if (remaining_sum + j) % 3 == 0 and j != int(S[i]):

                # If yes increment
                # the value of the count
                count += 1

    return count


S = "022"
print(solution(S))
