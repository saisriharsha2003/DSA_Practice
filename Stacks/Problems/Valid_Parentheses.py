
def isValid(s: str) -> bool:
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in pairs.values():
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


def main():
    print(isValid("()"))       # True
    print(isValid("()[]{}"))   # True
    print(isValid("(]"))       # False
    print(isValid("([)]"))     # False
    print(isValid("{[]}"))     # True
    print(isValid("("))        # False


if __name__ == "__main__":
    main()
