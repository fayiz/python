

def solution(A):
    sum_a = 0
    for number in A:
        sum_a += number

    max_num = len(A) + 1
    sum_expected = max_num * (max_num + 1) // 2
    return sum_expected - sum_a


arr = [5, 3, 2, 6, 1]
arr = [5, 3, 4, 2, 6, 1, 7]
arr = []
print(solution(arr))

