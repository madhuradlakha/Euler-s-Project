def square(a):
	return a*a;

def checkK(a,b,c):
	if (a+b+c) == 1000:
		return True
	
def checkE(a,b,c):
	if ((a*a)+(b*b)) == (c*c):
		return True
	
def run():
	for a in range(1,998):
		for b in range(1,998):
			for c in range(1,998):
				if checkK(a,b,c)==True and checkE(a,b,c)==True:
					print a*b*c
					
run()