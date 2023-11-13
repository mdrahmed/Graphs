def longest_common_consecutive_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1

    lccs = str1[end_index - max_length + 1 : end_index + 1]
    return lccs

if __name__ == "__main__":
    string1 = "AGGTTAB"
    string2 = "GGtext1TTXAYB"

    lccs = longest_common_consecutive_subsequence(string1, string2)

    if lccs:
        print(f"Longest Common Consecutive Subsequence: {lccs}")
    else:
        print("No common consecutive subsequence found.")

