# What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from 1 to N?
N = 3
def test(N,n):
    check = N
    ans = n
    found = False
    for i in range(1,check+1):
        if(ans % i == 0):
            found = True
        else:
            found = False
            break
    if(found == True):
        return found
                
def runner(N):
    checker = N
    while True:
        if(test(N,checker) == True):
            return checker
        else:    
            checker += 1
            test(N,checker)

print(runner(N))   