def longest_palindromic_subsequence(s):
    n = len(s)
    dp = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        dp.append(row)
    
    for i in range(n):
        dp[i][i] = 1

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j]:
                if l == 2:
                    dp[i][j] = 2  
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2  
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])  
    return dp[0][n - 1]  

string = str(input("Enter the string in lowercase letters: "))
print("Length of the longest palindromic subsequence:", longest_palindromic_subsequence(string))
