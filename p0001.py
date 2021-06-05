#We need to calculate all multiples of 3 and 5 that are lesser than given number N

N = 10

def test(N):
    total = sum(x for x in range(N) if (x % 3 == 0 or x % 5 == 0))
    return total 

    
print(test(N))