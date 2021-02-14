def solution(A):
    max_a = max(A)
    min_a = min(A)
    sum_a = sum(A)
    sum_remove = 0
    if min_a > 1:
        sum_remove = ((min_a-1) * min_a // 2)
    sum_expected = (max_a * (max_a + 1) // 2) - sum_remove
    return 1 if sum_a == sum_expected else 0
