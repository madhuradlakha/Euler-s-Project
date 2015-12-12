def range_prod(lo,hi):
	if lo+1<hi:
		mid = (lo+hi)//2
		return range_prod(lo,mid)*range_prod(mid+1,hi)
	if lo == hi:
		return lo
	return lo*hi

def fact(n):
	if n<2:
		return 1
	return range_prod(1,n)
	
def sumFact(n):
	temp1=n
	temp2=n
	sum=0
	while temp1:
		sum+=fact(temp1%10)
		temp1/=10
	if sum == temp2:
		return True
	else:
		return False
		
def run():
	sum1=0
	for i in range(3,1000000):
		if sumFact(i) == True:
			sum1+=i
	print sum1
		
run()