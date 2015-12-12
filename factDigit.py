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
	
def digitSum(n):
	t=n
	total=0
	while t!=0:
		total+=t%10
		t=t/10
	return total
		
	
ans = input("Enter value:")
result = fact(ans)
print digitSum(result)