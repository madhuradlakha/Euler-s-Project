def powx(base, exp):
	res=1
	while exp:
		if exp & 1 :
			res*=base
		exp>>=1
		base*=base
	return res
	
def run():
	sum=0
	for i in range(1,1001):
		sum+=powx(i,i)
	print sum%10000000000

		
run()