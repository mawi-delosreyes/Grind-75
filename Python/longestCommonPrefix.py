def longestCommonPrefix(strs: list[str]) -> str:

    strs.sort()
    pref_str = ""

    for i in range(min(len(strs[0]), len(strs[-1]))):

        if strs[0][i] != strs[-1][i]: break
        pref_str += strs[0][i]
    
    return pref_str

        
    




print(longestCommonPrefix(["flower","flow","flight"]))