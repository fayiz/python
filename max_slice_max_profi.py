

def solution(A):
    max_sum = 0
    temp_max_sum = 0
    for i in range(1, len(A)):
        d = A[i] - A[i-1] #delta
        temp_max_sum = max(d, temp_max_sum + d)
        max_sum = max(max_sum, temp_max_sum)
    return max_sum


#                      -2160,   112,   243,  -353,   354
print(solution([23171, 21011, 21123, 21366, 21013, 21367]))