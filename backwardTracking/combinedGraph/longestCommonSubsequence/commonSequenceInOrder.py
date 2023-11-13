def find_common_substrings(str1, str2):
    common_substrings = set()

    for i in range(len(str1)):
        for j in range(i + 1, len(str1) + 1):
            substring = str1[i:j]
            print(substring)
            if substring in str2:
                common_substrings.add(substring)

    return common_substrings

if __name__ == "__main__":
    string1 = "AGGTTAB"
    string2 = "GGtext1TTXAYB"
    print("common substrings in ",string1, " and ", string2)
    common_substrings = find_common_substrings(string1, string2)

    if common_substrings:
        print("Common Substrings:")
        for substring in common_substrings:
            if(len(substring) > 1):
                print(substring)
    else:
        print("No common substrings found.")

