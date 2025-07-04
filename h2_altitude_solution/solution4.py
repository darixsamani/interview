
def solution(X, Y, D):
    result = ((Y - X) - (Y - X)%D)//D
    return result if X + result * D >= Y else result +1