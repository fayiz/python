def solution(S):
    valid = True
    stack = []

    # stack.append("test")
    # print("Stack is empty....") if not stack else print("Stack is not empty!")
    # print("Stack Pop:" + stack.pop())
    # print("Stack is empty....") if not stack else print("Stack is not empty!")

    for c in S:
        if c == "(" or c == "[" or c == "{":
            stack.append(c)
        if c == ")":
            # valid = False if not stack or stack.pop() != "(" else valid
            if not stack or stack.pop() != "(":
                valid = False
        if c == "}":
            valid = False if not stack or stack.pop() != "{" else valid
        if c == "]":
            valid = False if not stack or stack.pop() != "[" else valid

    return True if valid and not stack else False


print(solution('[({[]}){[](){([[[]]])}}]'))


# solution 2
def balance_check(s):
    chars = []
    matches = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in matches:
            if chars.pop() != matches[c]:
                return False
        else:
            chars.append(c)
    return chars == []


print(balance_check('[({[]}){[](){([[[]]])}}]'))
