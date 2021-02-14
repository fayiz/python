

def solution(K, A):
    count = 0
    total_length = 0
    for rope_length in A:
        total_length += rope_length
        if total_length >= K:
            count += 1
            total_length = 0
    return count


print(solution(4, [1, 2, 3, 4, 1, 1, 3]))
