
def solution(A, K):
    result = [None] * len(A)
    arr_len = len(A)
    for i in range(arr_len):
        index = (i+k) % arr_len
        print(index)
        result[index] = A[i]
    return result


arr = [3, 1, 2, 4, 8, 7]
arr = [1, 2, 4, 8, 7, 3]
k = 2
print(solution(arr, k))