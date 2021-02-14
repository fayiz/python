
#Equllibrium

def solution(A):
    sum_a = sum(A)
    sum_left = A[0]
    sum_right = sum_a - sum_left
    diff = abs(sum_left - sum_right)
    for i in range(1, len(A) - 1):
        sum_left += A[i]
        # sum_right -= A[i]
        sum_right = sum_a - sum_left
        diff_cur = abs(sum_left - sum_right)
        if diff > diff_cur:
            diff = diff_cur
    return diff


arr = [5, 3, 4, 2, 6, 1, 7]
arr = [3, 1, 2, 4, 3]
print(solution(arr))