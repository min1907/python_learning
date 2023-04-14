import math


def solution(direction, radius, X, Y):
    # Implement your solution here
    # if direction == "U" or direction == "D":
    #     x_max = radius*math.sin(math.radians(45))
    #     y_max = radius
    #     print("UD",x_max, y_max)
    # if direction == "L" or direction == "R":
    #     y_max = radius*math.sin(math.radians(45))
    #     x_max = radius
    #     print("LR",x_max, y_max)

    N = len(X)
    count = 0
    for i in range(N):
        if direction == "U":
            # print(count, abs(X[i]), Y[i])
            if (
                abs(X[i]) >= 0
                and Y[i] > 0
                and 45 <= math.degrees(math.atan(abs(X[i]) / Y[i])) <= 90
                and math.sqrt(X[i] ** 2 + Y[i] ** 2) <= radius
            ):
                count += 1

        elif direction == "D":
            if (
                abs(X[i]) >= 0
                and Y[i] < 0
                and 0 <= math.degrees(math.atan(abs(X[i]) / abs(Y[i]))) <= 45
                and math.sqrt(X[i] ** 2 + Y[i] ** 2) <= radius
            ):
                count += 1

        elif direction == "L":
            if (
                abs(Y[i]) >= 0
                and X[i] < 0
                and 45 <= math.degrees(math.atan(abs(X[i]) / abs(Y[i]))) <= 90
                and math.sqrt(X[i] ** 2 + Y[i] ** 2) <= radius
            ):
                count += 1

        elif direction == "R":
            if (
                abs(Y[i]) >= 0
                and X[i] > 0
                and 0 <= math.degrees(math.atan(abs(X[i]) / abs(Y[i]))) <= 45
                and math.sqrt(X[i] ** 2 + Y[i] ** 2) <= radius
            ):
                count += 1

    return count


# direction = "U"
# radius = 5
# X = [-1,-2,4,1,3,0]
# Y = [5,4,3,3,1,-1]

direction = "D"
radius = 10
X = [0, -3, 2, 0]
Y = [-10, -3, -7, -5]

# direction = "R"
# radius = 3
# X = [-2,3]
# Y = [0,1]

# return 2
print(solution(direction, radius, X, Y))
