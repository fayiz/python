

def solution(A, B):
    pre_end_segment = -1
    count = 0
    for i in range(len(A)):
        start_segment = A[i]
        end_segment = B[i]
        if start_segment > pre_end_segment:
            count += 1
            pre_end_segment = B[i]
    return count


print(solution([1, 3, 7, 9, 1], [5, 6, 8, 9, 10]))
print(solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
print(solution([], []))