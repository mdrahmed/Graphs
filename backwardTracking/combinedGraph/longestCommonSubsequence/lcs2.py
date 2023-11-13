def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    lcs = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the LCS matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    # Find the longest common subsequence in order
    i, j = m, n
    result = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            result.insert(0, str1[i - 1])
            i -= 1
            j -= 1
        else:
            if lcs[i - 1][j] > lcs[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return ' '.join(result)

# Example usage
str1 = "AGGTTAB"
str2 = "GGtext1TTAB"
result = longest_common_subsequence(str1, str2)
print(result)  

