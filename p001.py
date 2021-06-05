#We need to calculate all multiples of 3 and 5 that are lesser than given number N
#My initial attempt wasnt great so i took help from this wonderful article https://medium.com/@TheZaki/project-euler-1-multiples-of-3-and-5-c24cb64071b0
N = 10

def sum(n, k):
    d = n // k
    return k * (d * (d+1)) // 2

def test(n):
     return sum(n, 3) + sum(n, 5) - sum(n, 15)

    
print(test(N-1))