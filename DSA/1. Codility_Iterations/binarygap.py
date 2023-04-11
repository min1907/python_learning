def binaryGap(N):
    pre = dist = 0
    for i, c in enumerate(bin(N)[2:]):
        if c == "1":
            dist = max(dist, i - pre - 1)
            pre = i
    return dist


print(binaryGap(32))
