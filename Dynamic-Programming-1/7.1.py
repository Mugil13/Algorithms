def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Find the LCS by tracing back the table
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    lcs.reverse()

    return L[m][n], lcs

size_X = int(input("Enter the length of the first sequence: "))
size_Y = int(input("Enter the length of the second sequence: "))

X = []
Y = []

print("\n-----SEQUENCE 1-----\n")
for i in range(size_X):
    ele1 = str(input("Enter element " + str(i + 1) + " of sequence 1: "))
    X.append(ele1)

print("\n-----SEQUENCE 2-----\n")
for j in range(size_Y):
    ele2 = str(input("Enter element " + str(j + 1) + " of sequence 2: "))
    Y.append(ele2)

length, lcs = longest_common_subsequence(X, Y)
print("\nLength of the longest common subsequence is:", length)
print("Longest Common Subsequence is:", lcs)
