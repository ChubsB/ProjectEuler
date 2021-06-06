# Given a number N, find its largest Prime factor

N = 10


def primeChecker(x):
    for i in range(2, int(x/2)+1):
        if(x % i == 0):
            return False
    return True


def largestPrimeFactor(N):
    ans = N
    for i in range(2,N):
        if(primeChecker(i) == True and N % i == 0):
            ans = i
    return ans

print(largestPrimeFactor(N))
