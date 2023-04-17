def isValid(s: str) -> bool:
    N = len(s)
    if N % 2 == 1:
        return False
    matched = {")": "(", "}": "{", "]": "["}
    to_push = ["(", "[", "{"]
    stack = []

    for element in s:
        if element in to_push:
            stack.append(element)
        else:  # not element in to_push [")", "]", "}"]
            if len(stack) == 0:  # no more open bracket to close
                return False
            elif (
                matched[element] != stack.pop()
            ):  # close bracket is not have corresponding open bracket
                return False
    if len(stack) == 0:
        return True
    else:
        return False


s1 = "()"
s2 = "()[]{}"
s3 = "(]"
print(isValid(s3))
