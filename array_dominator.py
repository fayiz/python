#program to find leader element in an array which is greater then n/2


def solution(A):
    consecutive_size = 0
    candidate = 0
    for item in A:
        if consecutive_size == 0:
            candidate = item
            consecutive_size += 1
        elif candidate == item:
            consecutive_size += 1
        else:
            consecutive_size -= 1
    print(f"candidate: {candidate} occurrence: {A.count(candidate)}")
    if A.count(candidate) > (len(A) / 2):
        return A.index(candidate)
    else:
        return -1

print(solution([3, 3, 4, 5, 5, 4, 5, 4, 4, 4, 4]))
print("=====")
print(solution([3, 0, 4, 1, 1, 1, 1]))

