
def solution(A, k):
    k %= len(A)
    return A[-k:] + A[:-k]