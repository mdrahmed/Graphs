def lcs(S1, S2):
    m, n = len(S1), len(S2)
    L = [[0] * (n + 1) for i in range(m + 1)]

    # Building the L[m+1][n+1] matrix
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i - 1] == S2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Finding the LCS
    index = L[m][n]
    lcs_sequence = [""] * (index + 1)
    lcs_sequence[index] = ""

    i, j = m, n
    while i > 0 and j > 0:

        if S1[i - 1] == S2[j - 1]:
            lcs_sequence[index - 1] = S1[i - 1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs_sequence)


if __name__ == '__main__':
    S1 = "AGGTTXYABB"
    S2 = "Gtext1TTAYBB"
    lcs_sequence = lcs(S1, S2)
    print("str1: ", S1, "\nstr2", S2)
    print("Length of LCS is", len(lcs_sequence))
    print("Longest subsequence is:", lcs_sequence)
       
    #S1_file = "./hbw"  # Replace with the actual path to your file
    #S2_file = "./vgr"  # Replace with the actual path to your file

    #with open(S1_file, 'r') as file1, open(S2_file, 'r') as file2:
    #    S1 = file1.read()
    #    S2 = file2.read()
    #    lcs_sequence = lcs(S1, S2)
    #with open('output.txt', 'w') as file_:
    #    #file_.write("str1: " + S1 + "\nstr2: " + S2 + "\n")
    #    file_.write("Length of LCS is " + str(len(lcs_sequence)) + "\n")
    #    file_.write("Longest subsequence is: " + lcs_sequence + "\n")
