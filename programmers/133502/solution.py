def solution(ingredient):
    hamburger = 0

    stack = []
    for i in ingredient:
        stack.append(i)

        if 4 <= len(stack):
            if can_wrap_hamburger(stack):
                hamburger += 1

                for _ in range(0, 4):
                    stack.pop()

    return hamburger


def can_wrap_hamburger(stack):
    if stack[len(stack) - 4] == 1 and stack[len(stack) - 3] == 2 and \
            stack[len(stack) - 2] == 3 and stack[len(stack) - 1] == 1:
        return True

    return False
