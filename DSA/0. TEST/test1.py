def solution(N):
    so_du = N % 9
    so_nguyen = N // 9
    if so_nguyen == 0:
        return so_du

    else:
        sum = so_du * (10**so_nguyen)
        so_nguyen -= 1
        while so_nguyen >= 0:
            # print(so_nguyen)
            sum += 9 * (10**so_nguyen)
            so_nguyen -= 1
    return sum


N = 50
print(solution(N))
