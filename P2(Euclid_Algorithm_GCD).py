
# ------------By Recursion---------------

# def gcd(m,n):
# 	if (m < n):
# 		(m,n) = (n,m)

# 	if(m%n == 0):
# 		return n 
# 	else:
# 		diff = m-n
# 		# diff > n ? Possibl!
# 		return(gcd(max(n,diff),min(n,diff)))

# -------------OR-----------------------

def gcd(m,n):
	if (m < n):
		(m,n) = (n,m)

	while (m%n != 0):
		diff = m-n
		# diff > n ? Possibl!
		(m,n) = (max(n,diff),min(n,diff))

	return n

# ---------------Using remainder(More simplofied)------------------ 

def gcd(m,n):
	if (m < n):
		(m,n) = (n,m)

	if(m%n == 0):
		return n
	else:
		gcd(n,m%n) # m%n < n
	return n

m = int(input("Enter first number m:"))
n = int(input("Enter first number n:"))
print("GCD of " + str(m) + " and " + str(n) + " is " + str(gcd(m, n)))
