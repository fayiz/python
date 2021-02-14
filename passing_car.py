
def solutions(A):
    sum_suffix = [0] * (len(A) + 1)
    count = 0
    for i in range(len(A) - 1, -1, -1):
        sum_suffix[i] = A[i] + sum_suffix[i+1]

    for i in range(len(A)):
        if A[i] == 0:
            count += sum_suffix[i]
        if count > 1000000000:
            return -1

    return count




print(solutions([0, 1, 0, 1, 1]))