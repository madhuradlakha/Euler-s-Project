def square(a):
	sum1=0
	print a
	for i in range(1,a+1):
		sum1+=i*i
	return sum1
	
def fullSquare(a):
	res=0
	for j in range(1,a+1):
		res+=j
	return res*res
	
ans=input("Enter number:")
final = square(ans)
final1 = fullSquare(ans)
print final
print final1
result = final1- final
print "Answer: %d"%(result)