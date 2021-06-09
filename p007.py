#What is the Nth prime number?

def primechecker(n):
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True

def test(limit):
	Count = 1
	currentPrime = 2
	while True:
		if(primechecker(currentPrime) == True):
			if(Count == limit):
				break
			else:
				Count += 1
				currentPrime +=1
		else:
			currentPrime += 1
	return currentPrime
	
print(test(6))