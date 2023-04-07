def solution(A, B):
    alive_count = 0
    down_stream_arr = []
    down_stream_count = 0

    for i in range(len(A)):
        if B[i] == 1:
            down_stream_arr.append(A[i])
            down_stream_count += 1
        else:  # if B[i] == 0
            while down_stream_count != 0:  # there are down stream fishes
                # this fish has to fight with fish down stream
                if down_stream_arr[-1] < A[i]:
                    down_stream_count -= 1
                    down_stream_arr.pop()
                else:
                    # Lose and die
                    break  # out of while loop and continue with next fish (next i)
            if down_stream_count == 0:
                # this up stream fish win and eat all down stream fishes or there is no more down stream fish that this fish need to fight and it's alive
                alive_count += 1

        # print(i, down_stream_arr, alive_count)

    if down_stream_count > 0:
        return alive_count + down_stream_count
    else:
        return alive_count


A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
print(solution(A, B))
