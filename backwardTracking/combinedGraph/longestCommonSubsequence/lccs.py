#def find_common_substrings(str1, str2):
#    common_substrings = set()
#
#    # Find all possible substrings in the first string
#    for i in range(len(str1)):
#        for j in range(i + 1, len(str1) + 1):
#            substring = str1[i:j]
#
#            # Check if the substring is present in the second string
#            if substring in str2:
#                common_substrings.add(substring)
#
#    return common_substrings

def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))

def lccs(a, b):
    possible = []
    if a[0] == b[0]:
        possible.append(lcs(a[1:], b[1:], len(a[1:]), len(b[1:])))
    possible.append(lcs(a[1:], b, len(a[1:]), len(b)))
    possible.append(lcs(a, b[1:], len(a), len(b[1:])))
    #return longest_string(possible)
    return possible

if __name__ == "__main__":
    string1 = "AGGTTAB"
    string2 = "GGtext1TTXAYB"	
    print("Common substrings between ",string1, " and ", string2)
    common_substrings = lccs(string1, string2)

    if common_substrings:
        print("Common Substrings:")
        for substring in common_substrings:
            print(substring)
    else:
        print("No common substrings found.")

