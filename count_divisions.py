from math import ceil, floor


def solution(A, B, K):
    possible_start = ceil(A/K)
    possible_end = floor(B/K)
    return possible_end - possible_start + 1


print(solution(3, 13, 4))