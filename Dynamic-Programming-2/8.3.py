def minimum(x,y,z):
	return min(x,min(y,z))

def edit(X,Y,m,n):
	dp=[[0 for i in range(n+1)] for j in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if i == 0:
				dp[i][j] = j
			elif j == 0:
				dp[i][j] = i
			elif X[i-1] == Y[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = 1 + minimum(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
	return dp[m][n]
	
X = input("Enter string 1: ")
Y = input("Enter string 2: ")
print("The number of operations to edit the strings is ",edit(X, Y, len(X), len(Y)))