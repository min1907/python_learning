# from string import List
def longestCommonPrefix(strs) -> str:
    shortest = min(strs, key=len)  # flow
    # print(list(enumerate(shortest))) #[(0, 'f'), (1, 'l'), (2, 'o'), (3, 'w')]
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest  # testcase strs3 = [""] -> len = 1 -> return ""


strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]
strs3 = [""]

print(longestCommonPrefix(strs2))
