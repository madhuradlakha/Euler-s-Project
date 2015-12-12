def fib(n):
	a=1
	b=1
	if n<=1 :
		return n
	for i in range(3,n+1):
		c=a+b
		a=b
		b=c
	return b
	
def run():
	i=1
	while (len(str(fib(i)))!=1000):
		i+=1
	print i
	
run()