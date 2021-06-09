# Find the absolute difference between the sum of the squares of the first  natural numbers and the square of the sum.

N = 10

def test(N):
	SquareSum = 0
	SumSquare = 0
	for i in range(1,N+1):
		SquareSum += i*i
		SumSquare += i
	SumSquare = SumSquare * SumSquare
	return SumSquare - SquareSum

print(test(N))
