# Find the largest palindrome made from the prodctu of two 3-digit numbers which is less than N

N = 101101


def FindPalindrome(s):
    temp = s
    rev = 0
    while(s>0):
        dig = s%10
        rev = rev * 10 + dig
        s = s//10
    if(temp == rev):
        return True
    else:
        return False


def FindProduct(y):
    for j in range(100, 1000):
        for k in range(100, 1000):
            if(j*k == y):
                return True
    return False


def test(n):
    for i in range(n, 0, -1):
        if(FindPalindrome(i) == True):
            if(FindProduct(i) == True):
                return i
    return "No Answer"

print(test(N-1))
