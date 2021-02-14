
def find_gcd(a, b):
    if b == 0:
        return a
    else:
        #print(find_gcd(b, a % b))
        return find_gcd(b, a % b)


def solutions(N, M):
    return N // find_gcd(N, M)


print(solutions(10, 4))