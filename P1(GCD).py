# def gcd(m,n):
# 	fm = []
# 	for i in range(1,m+1):
# 		if(m%i == 0):
# 			fm.append(i)

# 	fn = []
# 	for j in range(1,n+1):
# 		if(n%j == 0):
# 			fn.append(j)

# 	cf = []
# 	for f in fm:
# 		if (f in fn):
# 			cf.append(f)

# 	return cf[-1]
	
# ----------------------Better one--------------------#

# def gcd(m,n):
# 	for i in range(1,min(m,n) + 1):
# 		if m % i == 0 and n % i == 0:
# 			gcd = i

# 	return gcd

# -----------------------OR-----------------------------#

def gcd(m,n):
	i = min(m, n) + 1;
	while(i>0):
		if m % i == 0 and n % i == 0:
			return i 
		else:
			i -= 1

m = int(input("Enter first number m:"))
n = int(input("Enter first number n:"))
print("GCD of " + str(m) + " and " + str(n) + " is " + str(gcd(m, n)))
