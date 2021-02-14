
def solution(A, B):
    stack = []
    survivors = 0
    for i in range(len(A)):
        weight = A[i]
        if B[i] == 1:
            stack.append(weight)
        else:
            weightdown = stack.pop() if stack else -1
            # print(f"{weight} {weightdown}")
            while weightdown != -1 and weightdown < weight:
                weightdown = stack.pop() if stack else -1
            if weightdown == -1:
                survivors +=1
            else:
                stack.append(weightdown)

    return survivors + len(stack)





fish_size = [4, 8, 2, 6, 7]
fish_direction = [0, 1, 1, 0, 0] # 0: Up Stream(moving left)  1: down stream(moving right)
print(solution(fish_size, fish_direction))

fish_size = [4, 2, 2, 1, 5]
fish_direction = [0, 1, 0, 0, 0] # 0: Up Stream(moving left)  1: down stream(moving right)
print(solution(fish_size, fish_direction))