# Given a standard Fibonnaci Sequence, find the sum of even-valued terms that do need exceed some given integer N

N = 100


def EvenChecker(x):
    if(x % 2 == 0):
        return True
    else:
        return False


def SumCalculator(n):
    temp = 0
    s1 = 0
    s2 = 1
    EvenSum = 0
    while True:
        temp = s1 + s2
        if(temp > n):
            break
        s1 = s2
        s2 = temp
        if(s2 % 2 == 0):
            EvenSum += s2
    return EvenSum


def test(N):
    print(SumCalculator(N))

test(N)

