"""
Given two strings needle and haystack,
return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
"""


def strStr(haystack: str, needle: str) -> int:
    M = len(haystack)
    N = len(needle)
    if N > M:
        return -1
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            if haystack[i : i + N] == needle:
                # print("a")
                return i
            else:
                # print("b")
                continue
        else:
            # print("c")
            continue
    return -1


# haystack = "sadbutsad"
# needle = "sad"

haystack = "hello"
needle = "ll"

print(strStr(haystack, needle))

# print(haystack[0:3], needle)
