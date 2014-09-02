import sys
userinput = int(sys.argv[1]) 

def cond(x):
	if x%3==0 and x%5==0:
		return 'FizzBuzz'
	elif x%3==0:
		return 'Fizz'
	elif x%5==0:
		return 'Buzz'
	else:
		return x


newlist = [cond(i) for i in range(1,userinput)]

print newlist
